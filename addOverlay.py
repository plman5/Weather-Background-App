from PIL import Image

def add_weather_overlay(population, weatherCondition):
    # Set the target size for all images
    target_width = 500
    target_height = 500

    # Open and resize each image
    for filename in ['town.jpg', 'small_city.jpg', 'big_city.jpg', 'biggest_city.jpg']:
        img = Image.open(filename)
        img = img.resize((target_width, target_height))
        new_filename = filename
        img.save(new_filename)
 
    # Load the city jpg image based on the population of the city
    if population <= 60000:
        base_image = Image.open("town.jpg").convert("RGBA")
    elif population <= 200000:
        base_image = Image.open("small_city.jpg").convert("RGBA")
    elif population <= 1000000:
        base_image = Image.open("big_city.jpg").convert("RGBA")
    elif population > 1000000:
        base_image = Image.open("biggest_city.jpg").convert("RGBA")
    

    # Load the weather overlay image based on the weather condition
    if weatherCondition == "Sunny":
        overlay_image = Image.open("sun_overlay.png").convert("RGBA")
    elif weatherCondition == "Cloudy":
        overlay_image = Image.open("cloud_overlay.png").convert("RGBA")
    elif weatherCondition == "Rainy":
        overlay_image = Image.open("rain_overlay.png").convert("RGBA")
    elif weatherCondition == "Snowy":
        overlay_image = Image.open("snow_overlay.png").convert("RGBA")
    else:
        # Default to no overlay if the weather condition is not recognized
        return base_image

    # Resize the overlay image to match the size of the base image
    overlay_image = overlay_image.resize(base_image.size/3)

    # Combine the base image and overlay image
    result_image = Image.alpha_composite(base_image, overlay_image)

    # Return the modified image
    return result_image
