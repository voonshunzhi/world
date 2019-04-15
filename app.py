from world import app;
from world.models.models import Language,CountryLanguage,City,Country;
from flask import render_template,request,redirect,url_for,abort;
import csv
from world import db;

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/search")
def search():
    search = request.args.get('search');
    languages = Language.query.filter(Language.language.like('%' + search.title() +'%')).distinct(Language.language).group_by(Language.id,Language.language).all()
    countries = Country.query.filter(Country.country_name.like('%' + search.title() + '%')).distinct(Country.country_name).group_by(Country.id,Country.country_name,Country.country_code).all()
    cites = City.query.filter(City.city_name.like('%' + search.title() + '%')).distinct(City.city_name).group_by(City.id,City.city_name).all()
    totalLength = len(cites + countries + languages)
    results = "result" if len(languages) == 0 or languages == 1 else "results"
    return render_template("search.html",totalLength=totalLength,result=results,search=search,countries=countries,languages=languages,cities=cites);

@app.route("/country/<id>")
def country(id):
    country = Country.query.get(id)
    return render_template("country.html",country=country)

@app.route("/language/<id>")
def language(id):
    language = Language.query.get(id)
    languages = Language.query.filter_by(language=language.language).distinct(Language.country_code).group_by(Language.id,Language.country_code).all()
    print(languages)
    return render_template("language.html",language=language,languages=enumerate(languages))

@app.route("/city/<id>")
def city(id):
    city = City.query.get(id)
    return render_template("city.html",city=city)

@app.route("/update/city/<id>",methods=['GET','POST'])
def updateCity(id):
    city = City.query.get(id)
    if request.method == 'GET':
        return render_template("update/city.html",city=city)
    else:
        city.city_name = request.form['city_name']
        city.province = request.form['province']
        city.population = request.form['population']
        db.session.commit();
        return redirect(url_for('city',id=city.id),code=302)

@app.route("/update/country/<id>",methods=['GET','POST'])
def updateCountry(id):
    country = Country.query.get(id)
    if request.method == 'GET':
        return render_template("update/country.html",country=country)
    else:
        country.continent = request.form['continent']
        country.region = request.form['region']
        country.area = request.form['area'];
        country.year_of_independence = request.form['year_of_independence'];
        country.population = request.form['population'];
        country.life_expectancy = request.form['life_expectancy']
        country.gnp = request.form['gnp'];
        country.gnpid = request.form['gnpid'];
        country.alternative_name = request.form['alternative_name'];
        country.ruling_system = request.form['ruling_system'];
        country.founder = request.form['founder'];
        country.iso_code = request.form['iso_code'];
        db.session.commit();
        return redirect(url_for('country',id=country.country_code),code=302)

@app.route("/update/language/<id>",methods=['GET','POST'])
def updateLanguage(id):
    language = Language.query.get(id);
    if request.method == 'GET':
        return render_template('update/language.html',language=language);
    else:
        language.percentage_of_use = request.form['percentage_of_use']
        db.session.commit();
        return redirect(url_for('language',id=language.id),code=302)

@app.route("/delete/country/<id>",methods=['POST'])
def deleteCountry(id):
    if request.method == 'POST':
        country = Country.query.get(id);
        languages = Language.query.filter_by(country_code=id);
        for language in languages:
            db.session.delete(language);
            db.session.commit();
        db.session.delete(country);
        db.session.commit();
        return redirect(url_for('index'));
    else:
        return abort(404)
    
if __name__ == "__main__":
    app.run(debug=True);    