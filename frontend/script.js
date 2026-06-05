function ShowMessage() {
    document.getElementById("Message").textContent = "Thank you for visiting local biz connect.";
    document.getElementById("sendMessage").style.display = "none"; // Hide the button after click
}

function submitEnquiry(event){
    event.preventDefault(); // Prevent form submission
    const name = document.getElementById("studentName").value.trim();
    const email = document.getElementById("studentEmail").value.trim();
    const service = document.getElementById("service").value;
    const message = document.getElementById("message").value.trim();

    if(name === "" || email === "" || service === "" || message === ""){
        document.getElementById("formMessage").textContent = "Please fill in all fields.";
        document.getElementById("formMessage").style.color = "red";
    } else {
        formMessage.textContent = "Thank you, " + name + "! Your enquiry has been recorded for the Day 2 demo.";
    formMessage.style.color = "#123c69";
    }
}