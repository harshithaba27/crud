const API = "/students";
const AI_API = "/ask";
let editingId = null;

// LOAD STUDENTS
async function loadStudents() {
    const loading = document.getElementById("loading");
    loading.style.display = "block";
    try {
        const res = await fetch(API);
        const data = await res.json();

        const list = document.getElementById("list");
        list.innerHTML = "";

        data.forEach(student => {
            const li = document.createElement("li");
            li.innerHTML = `
                <div class="student-info">
                    <span class="student-name">${student.name}</span>
                    <span class="student-email">${student.email}</span>
                </div>
                <div class="actions">
                    <button onclick="editStudent(${student.id}, '${student.name}', '${student.email}')">Edit</button>
                    <button class="btn-delete" onclick="deleteStudent(${student.id})">Delete</button>
                </div>
            `;
            list.appendChild(li);
        });
    } catch (err) {
        console.error("Failed to load students", err);
    } finally {
        loading.style.display = "none";
    }
}

// ADD/UPDATE STUDENT
async function addStudent() {
    const name = document.getElementById("name").value.trim();
    const email = document.getElementById("email").value.trim();

    if (!name || !email) {
        alert("Please fill in all fields");
        return;
    }

    const payload = { name, email };
    const btn = document.getElementById("submitBtn");
    btn.disabled = true;
    btn.textContent = "Processing...";

    try {
        if (editingId) {
            await fetch(`${API}/${editingId}`, {
                method: "PUT",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify(payload)
            });
            editingId = null;
        } else {
            await fetch(API, {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify(payload)
            });
        }

        document.getElementById("name").value = "";
        document.getElementById("email").value = "";
        btn.textContent = "Add Student";
        document.getElementById("cancelBtn").style.display = "none";
        loadStudents();
    } catch (err) {
        alert("Error saving student");
    } finally {
        btn.disabled = false;
    }
}

function editStudent(id, name, email) {
    editingId = id;
    document.getElementById("name").value = name;
    document.getElementById("email").value = email;
    document.getElementById("submitBtn").textContent = "Update Student";
    document.getElementById("cancelBtn").style.display = "inline-block";
}

function cancelEdit() {
    editingId = null;
    document.getElementById("name").value = "";
    document.getElementById("email").value = "";
    document.getElementById("submitBtn").textContent = "Add Student";
    document.getElementById("cancelBtn").style.display = "none";
}

async function deleteStudent(id) {
    if (confirm("Are you sure you want to delete this record?")) {
        await fetch(`${API}/${id}`, {
            method: "DELETE"
        });
        loadStudents();
    }
}

// AI CHAT FUNCTIONS
async function askAI() {
    const input = document.getElementById("chatInput");
    const query = input.value.trim();
    if (!query) return;

    appendMessage('user', query);
    input.value = "";
    
    const loading = document.getElementById("aiLoading");
    loading.style.display = "block";

    try {
        const res = await fetch(AI_API, {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ query })
        });
        const data = await res.json();
        
        if (data.answer) {
            appendMessage('ai', data.answer);
        } else {
            appendMessage('ai', "Sorry, I encountered an error: " + (data.error || "Unknown error"));
        }
    } catch (err) {
        appendMessage('ai', "Could not connect to the AI service. Make sure Ollama is running.");
    } finally {
        loading.style.display = "none";
    }
}

function appendMessage(sender, text) {
    const container = document.getElementById("chatMessages");
    const div = document.createElement("div");
    div.className = `chat-message message-${sender}`;
    div.textContent = text;
    container.appendChild(div);
    container.scrollTop = container.scrollHeight;
}

function handleChatKey(event) {
    if (event.key === "Enter") {
        askAI();
    }
}

// Initialize
loadStudents();
