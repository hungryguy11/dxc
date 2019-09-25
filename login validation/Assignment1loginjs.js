var mailid = String(document.getElementById("emailid").value);
var uname = String(document.getElementById("username").value);
var passw = String(document.getElementById("psw").value);
var passc = String(document.getElementById("c-psw").value);
var phoneno = String(document.getElementById("phoneno").value);

var u = document.getElementById("user");
var p = document.getElementById("pass");
var c = document.getElementById("c-pass");
var e = document.getElementById("e-id");
var ph = document.getElementById("phno");
var b = document.getElementById("box");

var mailformat = /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/;
var pass = /^(?=.*[0-9])(?=.*[a-z])(?=.*[A-Z])(?=.*@).{8,}$/;
var phone = /^(?=.*[0-9])+$/;

function checkdetails() {

    if (uname.length == 0) {
        u.innerHTML = '<h5 class="text-danger">Username is Mandatory</h5>';
    }
    if (passw.length == 0) {
        p.innerHTML = '<h5 class="text-danger">Password is Mandatory</h5>';
    }
    if (mailid.length == 0) {
        e.innerHTML = '<h5 class="text-danger">Email Id is Mandatory</h5>';
    }
    if (phoneno.length == 0) {
        ph.innerHTML = '<h5 class="text-danger">Phone number is Mandatory</h5>';
    }

    if (phoneno.length != 10) {
        ph.innerHTML = '<h5 class="text-danger">Phone no must be 10 digits </h5>';

    }
    if (phone.match) {
        ph.innerHTML = '<h5 class="text-danger">Number format incorrect</h5>';
    }


    if (mailid.match(mailformat)) {
        if ((phoneno.match(phone))) {
            if (passw.match(pass)) {
                if (passw == passc) {
                    alert("Welcome " + uname);
                    b.innerHTML = '<div class="box alert alert" style="background-color:lightgreen; transparent:30%"><center>Login Successful</center></div>';
                } else {
                    c.innerHTML = '<h5 class="text-danger">Password does not match</h5>'
                }
            } else {
                b.innerHTML = '<div class="box" style="background-color:red;transparent:30%"><center>Login Failed</center></div>';
            }
        } else {
            ph.innerHTML = '<h5 class="text-danger">Number format incorrect</h5>';
        }

    } else {
        alert("Invalid Email Id");
        b.innerHTML = '<div class="box" style="background-color:red;transparent:30%"><center>Login Failed</center></div>';
    }

}











console.log(uname);
console.log(passw);