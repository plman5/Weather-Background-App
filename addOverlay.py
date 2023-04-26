from PIL import Image
import io
import base64

def add_weather_overlay(population, weatherCondition):
    # Set the target size for all images
    target_width = 100
    target_height = 200

    # Open and resize each image
    for filename in ['img/town.jpg', 'img/small_city.jpg', 'img/big_city.jpg', 'img/biggest_city.jpg']:
        img = Image.open(filename)
        img = img.resize((target_width, target_height))
        new_filename = filename
        img.save(new_filename)
 
    # Load the city jpg image based on the population of the city
    if population <= 60000:
        base_image = Image.open("img/town.jpg").convert("RGBA")
    elif population <= 200000:
        base_image = Image.open("img/small_city.jpg").convert("RGBA")
    elif population <= 1000000:
        base_image = Image.open("img/big_city.jpg").convert("RGBA")
    elif population > 1000000:
        base_image = Image.open("img/biggest_city.jpg").convert("RGBA")
    
    #Convert the weather condition to lowercase
    weatherCondition = weatherCondition.lower();

    # Load the weather overlay image based on the weather condition
    if "sun" in weatherCondition:
        overlay_image = Image.open("img/sun_overlay.png").convert("RGBA")
    elif "cloud" in weatherCondition:
        overlay_image = Image.open("img/cloud_overlay.png").convert("RGBA")
    elif "rain" in weatherCondition:
        overlay_image = Image.open("img/rain_overlay.png").convert("RGBA")
    elif "snow" in weatherCondition:
        overlay_image = Image.open("img/snow_overlay.png").convert("RGBA")
    elif "wind" in weatherCondition:
        overlay_image = Image.open("img/wind_overlay.png").convert("RGBA")
    elif "overcast" in weatherCondition:
        overlay_image = Image.open("img/overcast_overlay.png").convert("RGBA")
    elif "storm" in weatherCondition:
        overlay_image = Image.open("img/storm_overlay.png").convert("RGBA")
    else:
        # Default to no overlay if the weather condition is not recognized
        return base_image

    # Resize the overlay image to match the size of the base image
    size=overlay_image.size
    # Determine the scale factor based on the target size and the original size
    scale_factor = min(target_width/size[0], target_height/size[1])

    # Calculate the new size based on the scale factor
    new_size = (int(size[0]*scale_factor), int(size[1]*scale_factor))

    # Resize the image
    overlay_image = overlay_image.resize(new_size)

    # Combine the base image and overlay image
    result_image = Image.alpha_composite(base_image, overlay_image)

    # Convert the image to a base64 string
    img_buffer = io.BytesIO()
    result_image.save(img_buffer, format='PNG')
    img_str = base64.b64encode(img_buffer.getvalue()).decode()

    # Return the modified image as a base64 string
    return img_str
