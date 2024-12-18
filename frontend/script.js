const logoInput = document.getElementById('logo_input');
const logoDisplay = document.getElementById('logo_display');
const createLogoBtn = document.getElementById('create_logo_btn');
const downloadLogo = document.getElementById('download_logo');
const hamburger = document.getElementById('hamburger');
const sidebarMenu = document.querySelector('.sidebar_menu');
const closeMenuBtn = document.getElementById('close_menu_btn');
const signupBtn = document.getElementById('signup_btn');
const loginBtn = document.getElementById('login_btn');
const modal = document.getElementById('form_modal');
const formArea = document.getElementById('form_area');
const closeModalBtn = document.querySelector('.close_modal_btn');
const backendUrl = 'http://127.0.0.1:8000'

createLogoBtn.addEventListener('click', function() {
    const logoText = logoInput.value;
    const username = "current_user";

    if (logoText) {
        const requestBody = {
            username: username,
            prompt: logoText
        };

        fetch('${backendUrl}/generate', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(requestBody)
        })
        .then(response => response.json())
        .then(data => {
            if (data.image_name) {
                const imageUrl = `http://${backendUrl}/${data.image_name}`;
                logoDisplay.textContent = logoText;
                downloadLogo.href = imageUrl;
                downloadLogo.textContent = "Download Logo";
            } else {
                console.error('Logo creation failed:', data);
            }
        })
        .catch(error => console.error('Error:', error));
    }
});

hamburger.addEventListener('click', function() {
    sidebarMenu.classList.toggle('show');
});

closeMenuBtn.addEventListener('click', function() {
    sidebarMenu.classList.remove('show');
});

signupBtn.addEventListener('click', function() {
    formArea.innerHTML = `
        <h2>Sign Up</h2>
        <input type="text" placeholder="Enter your username" id="signupUsername"/>
        <input type="email" placeholder="Enter your email" id="signupEmail"/>
        <input type="password" placeholder="Enter your password" id="signupPassword"/>
        <button id="submitSignup">Submit</button>
    `;
    modal.style.display = 'block';

    document.getElementById('submitSignup').addEventListener('click', function() {
        const username = document.getElementById('signupUsername').value;
        const email = document.getElementById('signupEmail').value;
        const password = document.getElementById('signupPassword').value;

        fetch('${backendUrl}/signup', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ username, email, password })
        })
        .then(response => response.json())
        .then(data => {
            if (data.message) {
                alert('Signup successful!');
                modal.style.display = 'none';
            } else {
                console.error('Signup failed:', data);
            }
        })
        .catch(error => console.error('Error:', error));
    });
});

loginBtn.addEventListener('click', function() {
    formArea.innerHTML = `
        <h2>Login</h2>
        <input type="text" placeholder="Enter your username or email" id="loginIdentifier"/>
        <input type="password" placeholder="Enter your password" id="loginPassword"/>
        <button id="submitLogin">Login</button>
    `;
    modal.style.display = 'block';

    document.getElementById('submitLogin').addEventListener('click', function() {
        const identifier = document.getElementById('loginIdentifier').value;
        const password = document.getElementById('loginPassword').value;

        fetch('${backendUrl}/login', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ identifier, password })
        })
        .then(response => response.json())
        .then(data => {
            if (data.message) {
                alert('Login successful!');
                modal.style.display = 'none';
            } else {
                console.error('Login failed:', data);
            }
        })
        .catch(error => console.error('Error:', error));
    });
});

closeModalBtn.addEventListener('click', function() {
    modal.style.display = 'none';
});

window.addEventListener('click', function(e) {
    if (e.target == modal) {
        modal.style.display = 'none';
    }
});