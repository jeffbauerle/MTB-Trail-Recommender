from flask import Flask, render_template, request, jsonify

from data_provider import get_regions, get_trails_by_region, get_recommended_trails_by_trail, get_recommended_trails_by_region_and_trail

app = Flask(__name__)

# home page
@app.route('/', methods =['GET','POST'])    
def index():
    regions = get_regions()
    return render_template('index.html', regions=regions)

@app.route('/trails', methods=['GET','POST'])
def trails():

    regions = get_regions()
    print(regions)
    return render_template('trails.html', regions=regions)
    
@app.route('/region', methods=['GET','POST'])
def region():
    region = request.args.get('region')    
    regions = get_regions()
    
    try:
        region_name = regions[region]    
    except:
        return region + " is not a valid region"
             
    trails = get_trails_by_region(region)        
    
    region_options = convert_regions_to_select_options(regions)
    return render_template('region.html',region_name=region_name, regions=region_options, trails=trails)

@app.route('/get_trails')
def get_trails():
    region = request.args.get('region')    
    if region:       
        trails = get_trails_by_region(region)        
        # print(trails)
    return jsonify(trails)

@app.route('/recommendations', methods=['GET','POST'])
def recommendations():    
    
    trail_id = request.form.get('trail')
    region = request.form.get('region')

    trails = get_recommended_trails_by_region_and_trail(region, trail_id, 5)
    regions = get_regions()
    region_name = regions[region]    
    original_trail = trails[0]
    recommended_trails = trails[1::]

    return render_template('recommendations.html',original_trail=original_trail, recommended_trails=recommended_trails, region_name=region_name)

def convert_regions_to_select_options(regions):
    options = []    
    for key,value in regions.items():
        options.append({'value':key, 'text': value})
    return options


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8105, threaded=True)