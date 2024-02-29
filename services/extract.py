def extract_google_maps_url_from_iframe(iframe):
    start_index = iframe.find("src=") + 5
    end_index = iframe.find('"', start_index)
    if start_index != -1 and end_index != -1:
        return iframe[start_index:end_index]
    return None
