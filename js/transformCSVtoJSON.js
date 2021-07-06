module.exports = function main(
    line = 'tampa, 106, january, null, null, 08-17-2019'
  ) {
    // [START composer_transform_csv_to_json]
  
    function transformCSVtoJSON(line) {
      var values = line.split(',');
      var properties = [
        'user_id',
        'search_keyword',
        'search_result_count',
        'created_at'
      ];
      var weatherInCity = {};
  
      for (var count = 0; count < values.length; count++) {
        if (values[count] !== 'null') {
          weatherInCity[properties[count]] = values[count];
        }
      }
  
      var jsonString = JSON.stringify(weatherInCity);
      return jsonString;
    }
  
    // [END composer_transform_csv_to_json]
  
    return transformCSVtoJSON(line);
  };
