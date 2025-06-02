    // Persistent user storage
    const initialUsers = [{username:'Cezara',password:'cezara123'},{username:'Raul',password:'raul123'}];
    let signUpUsers = JSON.parse(localStorage.getItem('signUpUsers')||'[]');
    const allUsers = () => initialUsers.concat(signUpUsers);

    // Site name animation
    document.addEventListener('DOMContentLoaded', () => {
      // already animated via CSS keyframes
    });

    // Modal controls
    const loginBtn = document.getElementById('loginBtn'),
          signUpBtn = document.getElementById('signUpBtn'),
          loginModal = document.getElementById('loginModal'),
          signUpModal = document.getElementById('signUpModal'),
          closeLogin = document.getElementById('closeLoginModal'),
          closeSignUp = document.getElementById('closeSignUpModal'),
          loginForm = document.getElementById('loginForm'),
          signUpForm = document.getElementById('signUpForm'),
          loginMsg = document.getElementById('loginMessage'),
          signUpMsg = document.getElementById('signUpMessage');

    loginBtn.onclick = () => { loginMsg.textContent=''; loginForm.reset(); loginModal.classList.add('active'); };
    closeLogin.onclick = () => loginModal.classList.remove('active');
    signUpBtn.onclick = () => { signUpMsg.textContent=''; signUpForm.reset(); signUpModal.classList.add('active'); };
    closeSignUp.onclick = () => signUpModal.classList.remove('active');

    // Sign Up logic
    signUpForm.onsubmit = e => {
      e.preventDefault();
      const u = signUpForm.username.value.trim(), p = signUpForm.password.value, c = signUpForm.confirmPassword.value;
      if (p !== c) {
        signUpMsg.textContent = 'Passwords do not match.';
      } else {
        signUpUsers.push({username: u, password: p});
        localStorage.setItem('signUpUsers', JSON.stringify(signUpUsers));
        signUpMsg.textContent = 'Account created!';
        signUpMsg.classList.add('success');
        setTimeout(() => signUpModal.classList.remove('active'), 800);
      }
    };

    // Login logic
    loginForm.onsubmit = e => {
      e.preventDefault();
      const u = loginForm.username.value.trim(), p = loginForm.password.value;
      const valid = allUsers().some(x => x.username === u && x.password === p);
      if (valid) {
        loginMsg.textContent = 'Welcome back!';
        loginMsg.classList.add('success');
        setTimeout(() => window.location.href = 'notebook.html', 800);
      } else {
        loginMsg.textContent = 'Invalid credentials.';
      }
    };

    // Start button ripple and action
    document.getElementById('startBtn').addEventListener('click', function(e) {
      e.preventDefault();
      const r = document.createElement('span'); r.className='ripple'; this.appendChild(r);
      const d = Math.max(this.offsetWidth, this.offsetHeight);
      r.style.width = r.style.height = d + 'px';
      r.style.left = e.clientX - this.getBoundingClientRect().left - d/2 + 'px';
      r.style.top = e.clientY - this.getBoundingClientRect().top - d/2 + 'px';
      r.addEventListener('animationend', () => r.remove());
      setTimeout(() => window.location.href='notebook.html', 300);
    });
