let department = document.getElementById("department").addEventListener('click', Department)
function Department()   {
    let dept = document.getElementById("department")
    let val = dept.value
    let txt = dept.options[dept.selectedIndex]
    $.ajax({
        type: 'POST',
        url: '/profile/<id>',
        data: {
            'text': txt
        },
        success: function response(){
            var val1 = response.pos1;
            var len1 = val1.length;
            var val2 = response.pos2;
            var len2 = val2.length;
            var desg = document.getElementById("designation")
            var manager = document.getElementById("yourmanager")
            if (len1>0)   {
                if(len2>0)  {
                    positions = "";
                    positions += "<option value='manager'>Manager</option>";
                    positions += "<option value='employee'>Employee</option>";
                    desg.innerHTML = positions;
                }
                else    {
                    positions = "";
                    positions += "option value='employee'>Employee</option>";
                    desg.innerHTML = positions;
                    manager.value = response.pos3;
                }
            }
            else    {
                positions = "";
                positions += "<option value='manager'>Manager</option>";
                positions += "<option value='employee'>Employee</option>";
                desg.innerHTML = positions;
            }
        },
    }); 
} 
