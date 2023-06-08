    function validateForm() {
        var prenom = document.forms["myForm"]["prenom"].value;
        var nom = document.forms["myForm"]["nom"].value;
        var telephone = document.forms["myForm"]["telephone"].value;

        // Expression régulière pour vérifier les chaînes de caractères
        var regexName = /^[A-Za-z]+$/;
        var regextelephone = /^(70|77|76|78|75)[0-9]{7}$/;

        // Vérification du prénom
        if (!regexName.test(prenom)) {
            alert("Le prénom ne doit contenir que des lettres.");
            return false;
        }

        // Vérification du nom
        if (!regexName.test(nom)) {
            alert("Le nom ne doit contenir que des lettres.");
            return false;
        }

        // Vérification du numéro de téléphone
        if (!regextelephone.test(telephone)) {
            alert("Le numéro de téléphone doit commencer par l'un des préfixes (70, 77, 76, 78, 75) et contenir exactement 9 chiffres.");
            return false;
        }
    }