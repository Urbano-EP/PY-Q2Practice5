from pyscript import document, display

def check_country(e):
    document.getElementById('output1').innerHTML = ""
    country = {
        "ph": "Philippines",
        "au": "Australia",
        "jp": "Japan",
        "fr": "France",
        "sg": "Singapore"
    }

    country_code = document.getElementById('countries').value

    #add a country
    country["ca"] = "Canada"

    display(country.get(country_code, "Country Code Not Found"), target = "output1")