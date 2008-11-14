function change_ea_visibility(){
    if(document.getElementById('OperationalProgramme').value == "EA"){
        //document.getElementById('archetypes-fieldname-EABiodiversity').style.visibility = 'visible'
        document.getElementById('archetypes-fieldname-EABiodiversity').style.display = 'block'
        document.getElementById('archetypes-fieldname-EABiodiversityOther').style.display = 'block'
        document.getElementById('archetypes-fieldname-EAClimateChange').style.display = 'block'
        document.getElementById('archetypes-fieldname-EAClimateChangeOther').style.display = 'block'
        document.getElementById('archetypes-fieldname-EAPOP').style.display = 'block'
        document.getElementById('archetypes-fieldname-EAPOPOther').style.display = 'block'
    }else{
        //document.getElementById('archetypes-fieldname-EAClimateChangeOther').style.visibility = 'hidden'
        document.getElementById('archetypes-fieldname-EABiodiversity').style.display = 'none'
        document.getElementById('archetypes-fieldname-EABiodiversityOther').style.display = 'none'
        document.getElementById('archetypes-fieldname-EAClimateChange').style.display = 'none'
        document.getElementById('archetypes-fieldname-EAClimateChangeOther').style.display = 'none'
        document.getElementById('archetypes-fieldname-EAPOP').style.display = 'none'
        document.getElementById('archetypes-fieldname-EAPOPOther').style.display = 'none'
    }
}

function set_ea_check_function(){
    change_ea_visibility()
    document.getElementById('OperationalProgramme').onchange=change_ea_visibility;
}


if(document.addEventListener){
        addEventListener('load', set_ea_check_function, false);
} else if(window.attachEvent){
        window.attachEvent('onload', set_ea_check_function);
}

