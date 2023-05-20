test = [
    [{'name': 'Laura Shigihara', 'type': 'artist'}],
    [{'name': 'Super Mario 64', 'type': 'artist'}, {'name': 'GMB Sound Team', 'type': 'artist'}]
]

result = []

for sublist in test:
    artists = []
    for artist_dict in sublist:
        artists.append(artist_dict['name'])
    print(artists)
    result.append(", ".join(artists))  # Convert sublist to a comma-separated string

print(result)