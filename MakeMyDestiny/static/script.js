async function signup() {
    let data = {
        username: document.getElementById("s_user").value,
        first: document.getElementById("s_first").value,
        last: document.getElementById("s_last").value,
        phone: document.getElementById("s_phone").value,
        email: document.getElementById("s_email").value,
        password: document.getElementById("s_pass").value
    };

    await fetch("/signup", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify(data)
    });

    alert("Account Created!");
}

async function login() {
    let data = {
        username: document.getElementById("username").value,
        password: document.getElementById("password").value
    };

    let res = await fetch("/login", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify(data)
    });

    let result = await res.json();

    if (result.status === "Login Success") {
        localStorage.setItem("user", data.username);

        // ADMIN CHECK
        if (data.username === "admin") {
            alert("Welcome Admin!");
            document.getElementById("adminPanel").style.display = "block";
        } else {
            alert("Welcome User!");
        }

    } else {
        alert(result.status);
    }
}
async function book() {
    let data = {
        username: localStorage.getItem("user"),
        service: document.getElementById("service").value,
        from: document.getElementById("from").value,
        to: document.getElementById("to").value,
        date: document.getElementById("date").value,
        persons: document.getElementById("persons").value,
        seat: document.getElementById("seat").value
    };

    await fetch("/book", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify(data)
    });

    alert("Booking Confirmed!");
}

async function viewAllBookings() {
    let res = await fetch("/allbookings");
    let data = await res.json();

    let output = document.getElementById("adminOutput");
    output.innerHTML = "<h3>All Bookings</h3>";

    data.forEach(b => {
        output.innerHTML += `
            <div style="background:#eee;padding:10px;margin:5px;border-radius:8px;">
                <b>User:</b> ${b.username} <br>
                <b>${b.service}</b> | ${b.from_loc} → ${b.to_loc} <br>
                Date: ${b.date} | Seat: ${b.seat}
            </div>
        `;
    });
}
function generateSeats() {
    let container = document.getElementById("seatContainer");
    container.innerHTML = "";

    for (let i = 1; i <= 20; i++) {
        let seat = document.createElement("button");
        seat.innerText = i;
        seat.style.margin = "5px";
        seat.style.width = "40px";
        seat.style.height = "40px";

        seat.onclick = function () {
            document.getElementById("seat").value = "Seat " + i;
        };

        container.appendChild(seat);
    }
}
window.onload = function () {
    generateSeats();
};
function logout() {
    localStorage.removeItem("user");
    alert("Logged out successfully!");
    location.reload();
}
window.onload = function () {
    let user = localStorage.getItem("user");

    if (user) {
        alert("Welcome back " + user);
    }
};