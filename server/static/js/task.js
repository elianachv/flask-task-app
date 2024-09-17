document.addEventListener('DOMContentLoaded', (event) => {

    const newTaskModal = document.getElementById('newTaskModal');
    const editTaskModal = document.getElementById('editTaskModal');
    const openNewTaskModalBtn = document.getElementById('openNewTaskModalBtn');
    const closeNewTaskModalBtn = document.getElementById('closeNewTaskModalBtn');
    const closeEditTaskModalBtn = document.getElementById('closeEditTaskModalBtn');

    openNewTaskModalBtn.onclick = function () {
        newTaskModal.style.display = 'block';
    }

    closeNewTaskModalBtn.onclick = function () {
        newTaskModal.style.display = 'none';
    }

    closeEditTaskModalBtn.onclick = function () {
        editTaskModal.style.display = 'none';
    }

    window.onclick = function (event) {
        if (event.target == newTaskModal) {
            newTaskModal.style.display = 'none';
        }

        if (event.target == editTaskModal) {
            editTaskModal.style.display = 'none';
        }
    }

   const  openEditTaskModal = function (id, title, description, status, deadline, user) {
        document.getElementById('task_id').value = id;
        document.getElementById('title').value = title;
        document.getElementById('description').value = description;
        document.getElementById('status').value = status;
        document.getElementById('deadline').value = deadline;
        user_element = document.getElementById('user')
        if (user_element) {
          document.getElementById('user').value = user;
        }
        editTaskModal.style.display = 'block';
    }

    document.querySelectorAll('.edit-btn').forEach(button => {
        button.addEventListener('click', (event) => {
            const id = button.getAttribute('data-id');
            const title = button.getAttribute('data-title');
            const description = button.getAttribute('data-description');
            const status = button.getAttribute('data-status');
            const deadline = button.getAttribute('data-deadline');
            const user = button.getAttribute('data-user');
            openEditTaskModal(id, title, description, status, deadline, user)
        });
    });

})