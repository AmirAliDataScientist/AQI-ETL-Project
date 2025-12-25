def extract_iaqi_data(city_name, city_payload):
    """
    Transforms raw city AQI payload into a flat record.
    If AQI data is missing or status is failed, pollutant values remain None.
    """

    # Base record (city should ALWAYS exist)
    record = {
        "city": city_name,
        "timestamp": None
    }

    # Safely access data block
    data_block = city_payload.get("data", {})

    # Safely extract timestamp
    time_info = data_block.get("time")
    if time_info:
        record["timestamp"] = time_info.get("iso")

    # Safely extract AQI block
    iaqi = data_block.get("iaqi", {})

    # Flatten AQI values (safe even if iaqi is empty)
    for pollutant, value_dict in iaqi.items():
        record[pollutant] = value_dict.get("v")

    return record

