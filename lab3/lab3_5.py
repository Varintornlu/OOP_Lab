record_collection = {
  2548: {
    'albumTitle': 'Slippery When Wet',
    'artist': 'Bon Jovi',
    'tracks': ['Let It Rock', 'You Give Love a Bad Name']
  },
  2468: {
    'albumTitle': '1999',
    'artist': 'Prince',
    'tracks': ['1999', 'Little Red Corvette']
  },
  1245: {
    'artist': 'Robert Palmer',
    'tracks': []
  },
  5439: {
    'albumTitle': 'ABBA Gold'
  }
}

def update_records(record, id, property, value):
  if id in record:
    album = record[id]

    if property != 'tracks':
        if value != '':
            album[property] = value
        else:
            album.pop(property, None)
    elif property == 'tracks':
        if 'tracks' not in album:
            album['tracks'] = []

        if value != '':
            album['tracks'].append(value)
        else:
            album.pop('tracks', None)

  return record






        

