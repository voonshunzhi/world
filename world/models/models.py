from world import db;

CountryLanguage = db.Table('CountryLanguage',
    db.Column('language_id', db.Integer, db.ForeignKey('language.id'), primary_key=True),
    db.Column('country_code', db.String(128), db.ForeignKey('country.country_code'), primary_key=True),
)

class Country(db.Model):

    __tablename__ = "country"

    id = db.Column(db.Integer);
    cities = db.relationship('City', backref='country',lazy=True,passive_deletes=True)
    country_code = db.Column(db.String(128),unique=True,primary_key=True)
    country_name = db.Column(db.String(128));
    continent = db.Column(db.String(128));
    region = db.Column(db.String(128));
    area = db.Column(db.Integer);
    year_of_independence = db.Column(db.Integer,nullable=True);
    population = db.Column(db.Float);
    life_expectancy = db.Column(db.Float,nullable=True);
    gnp = db.Column(db.Float);
    gnpid = db.Column(db.Float,nullable=True);
    alternative_name = db.Column(db.Text);
    ruling_system = db.Column(db.Text);
    founder = db.Column(db.Text);
    iso_code = db.Column(db.String(128))


    def __init__(self,country_code,country_name,continent,region,area,year_of_independence,population,life_expectancy,gnp,gnpid,alternative_name,ruling_system,founder,iso_code):
        self.country_code = country_code;
        self.country_name = country_name
        self.continent = continent;
        self.region = region;
        self.area = area;
        self.year_of_independence = year_of_independence;
        self.population = population;
        self.life_expectancy = life_expectancy
        self.gnp = gnp;
        self.gnpid = gnpid;
        self.alternative_name = alternative_name;
        self.ruling_system = ruling_system;
        self.founder = founder;
        self.iso_code = iso_code;

    def __repr__(self):
        return "This is the language of " + self.country_name;

class City(db.Model):

    __tablename__ = "city"
    id = db.Column(db.Integer, primary_key=True);
    city_name = db.Column(db.String(128));
    province= db.Column(db.String(128));
    population = db.Column(db.Float);
    country_code = db.Column(db.String(128), db.ForeignKey('country.country_code',ondelete='CASCADE'),nullable=False)

    def __init__(self,city_name,country_code,province,population):
        self.city_name = city_name;
        self.population = population;
        self.country_code = country_code;
        self.province = province;

    def __repr__(self):
        return "This is the language of " + self.city_name;

class Language(db.Model):

    __tablename__ = "language"

    id = db.Column(db.Integer, primary_key=True);
    country_code = db.Column(db.String(128))
    language = db.Column(db.String(128));
    official_language = db.Column(db.Boolean,default=False, nullable=False),
    percentage_of_use = db.Column(db.Float)

    def __init__(self,country_code,language,official_language,percentage_of_use):
        self.language = language;
        self.country_code = country_code;
        self.official_language = official_language;
        self.percentage_of_use = percentage_of_use;

    def __repr__(self):
        return "This is the language of " + self.language ;




