from PIL import Image

def add_weather_overlay(image_path, weatherCondition):
    # Load the base image
    base_image = Image.open(image_path).convert("RGBA")

    # Load the weather overlay image based on the weather condition
    if weatherCondition == "Sunny":
        overlay_image = Image.open("sunny.png").convert("RGBA")
    elif weatheCondition == "Cloudy":
        overlay_image = Image.open("cloudy.png").convert("RGBA")
    elif weatherCondition == "Rainy":
        overlay_image = Image.open("rainy.png").convert("RGBA")
    else:
        # Default to no overlay if the weather condition is not recognized
        return base_image

    # Resize the overlay image to match the size of the base image
    overlay_image = overlay_image.resize(base_image.size)

    # Combine the base image and overlay image
    result_image = Image.alpha_composite(base_image, overlay_image)

    # Return the modified image
    return result_image
