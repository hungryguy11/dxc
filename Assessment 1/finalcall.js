function checkdetails() {
    var uname = document.getElementById("uname").value;
    var psw = String(document.getElementById("psw").value);
    var cpsw = String(document.getElementById("cpsw").value);
    var name = document.getElementById("nam").value;
    var zip = document.getElementById("zip").value;
    var mail = document.getElementById("email").value;
    // var country = document.getElementById("country").value;
    var sex = document.getElementsByName("sex");
    var lang = document.getElementsByName("lang");


    var u = document.getElementById("u-id");
    var p = document.getElementById("pw");
    var cp = document.getElementById("cpw");
    var n = document.getElementById("names");
    var z = document.getElementById("zipc");
    var e = document.getElementById("e-id");
    var cntry = document.getElementById("reg");
    var g = document.getElementById("gender");
    var l = document.getElementById("language");
    var b = document.getElementById("result");


    var zipformat = /^[0-9]+$/;
    var mailformat = /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/;
    var nameformat = /^[A-Za-z]+$/;


    //for checkbox and radio button validation
    var count1 = 0,
        count2 = 0;

    for (i = 0; i < sex.length; i++) {
        if (sex[i].checked == false)
            count1++;
    }

    for (i = 0; i < lang.length; i++) {
        if (lang[i].checked == false)
            count2++;
    }
    console.log(count1, sex.length);
    console.log(count2, lang.length);
    // console.log(g, l);
    if (count1 == sex.length)
        g.innerHTML = '<p class="text-danger">Please select your gender</p>';
    if (count2 == lang.length)
        l.innerHTML = '<p class="text-danger">Please enter known language</p>';




    if (uname.length == 0)
        u.innerHTML = '<p class="text-danger">Please enter UserId</p>';
    if (psw.length == 0)
        p.innerHTML = '<p class="text-danger">Please enter password</p>';
    if (name.length == 0)
        n.innerHTML = '<p class="text-danger">Please enter you first name</p>';
    if (zip.length == 0)
        z.innerHTML = '<p class="text-danger">Please enter zipcode</p>';
    if (mail.length == 0)
        e.innerHTML = '<p class="text-danger">Please enter emailId</p>';

    //for datalist validation
    var val = $("#country").val();
    var obj = $("#region").find("option[value='" + val + "']");





    // if (lang[0].checked == true || lang[1].checked == true) {
    //     if (sex[0].checked == true ||sex[1].checked == true || sex[2] == checked) {
    // if (country != null) {
    if (obj != null && obj.length > 0) {
        if (name.match(nameformat)) {
            if (mail.match(mailformat)) {
                if (zip.match(zipformat)) {
                    if (uname.length > 5 && uname.length < 12) {
                        if (psw.length > 7 && psw.length < 12) {
                            if (cpsw == psw) {

                                b.innerHTML = '<div class="box alert alert" style="background-color:lightgreen; transparent:30%"><center>Successful</center></div>';
                            } else {
                                cp.innerHTML = '<p class="text-danger">Password does not match</p>';
                            }
                        } else {
                            p.innerHTML = '<p class="text-danger">Password must be of 7 - 12 characters</p>';
                        }
                    } else {
                        u.innerHTML = '<p class="text-danger">UserId must be of 5 - 12 characters</p>';
                    }
                } else {
                    z.innerHTML = '<p class="text-danger">Zipcode must be numerical</p>';
                }
            } else {
                e.innerHTML = '<p class="text-danger">Incorrect Email format</p>';
            }
        } else {
            n.innerHTML = '<p class="text-danger">Enter Alphabets only</p>';
        }
    } else {
        cntry.innerHTML = '<p class="text-danger">Please enter country</p>';
    }
    // } else {
    //     cntry.innerHTML = '<p class="text-danger">Please enter country</p>';
    // }
    //     } else {
    //         alert("gender");
    //         g.innerHTML = '<p class="text-danger">Please select your gender</p>'
    //     }
    // } else {
    //     alert("language");
    //     l.innerHTML = '<p class="text-danger">Please enter known language</p>'
    // }




}