from flask import Flask, render_template, send_from_directory

app = Flask(__name__)

# SEO Meta Data
app.config['SEO'] = {
    'title': 'J&D Associates | Premier Defense, Security & Maritime Technologies',
    'description': 'J&D Associates delivers world-class night vision systems, high-performance underwater vehicles, and specialized naval vessels for defense and commercial applications.',
    'keywords': 'Night Vision, Sea Chariot, Underwater Vehicles, Defense Technology, Maritime Security, J&D Associates, Electro-Optics'
}

@app.context_processor
def inject_seo():
    return {'seo': app.config['SEO']}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/marine')
def marine():
    return render_template('marine.html', title='Marine: Sea Chariots & Vessels')

@app.route('/aviation')
def aviation():
    return render_template('aviation.html', title='Aviation: Aircraft & Spare Parts')

@app.route('/electro-optics')
def electro_optics():
    return render_template('electro_optics.html', title='Electro-Optics: Night Vision & Lighting')

@app.route('/contact')
def contact():
    return render_template('contact.html', title='Contact J&D Associates')

@app.route('/sitemap.xml')
def sitemap():
    return send_from_directory(app.root_path, 'sitemap.xml', mimetype='application/xml')

@app.route('/robots.txt')
def robots():
    return send_from_directory(app.root_path, 'robots.txt', mimetype='text/plain')

if __name__ == '__main__':
    app.run(debug=True)