import requests

ENDPOINT = "http://localhost:8000/quotes"

# Create a quote
r = requests.post(ENDPOINT, json={"text": "Everything is practice.", "author": "Pele"})
assert r.status_code == 200
assert r.json()["message"] == "Added 'Everything is practice.' to quotes."
print("Create a quote run successfully.")

# # Verify that item "rock" has quantity 0
# r = requests.get(ENDPOINT + "?name=rock")
# assert r.status_code == 200
# assert r.json()["quantity"] == 0

# # Update item "rock" with quantity 100
# r = requests.put(ENDPOINT, json={"name": "rock", "quantity": 100})
# assert r.status_code == 200
# assert r.json()["message"] == "Updated rock."

# # Verify that item "rock" has quantity 100
# r = requests.get(ENDPOINT + "?name=rock")
# assert r.status_code == 200
# assert r.json()["quantity"] == 100

# Delete a quote "Everything is practice."
r = requests.delete(ENDPOINT, json={"text": "Everything is practice.", "author": "Pele"})
assert r.status_code == 200
assert r.json()["message"] == "Deleted 'Everything is practice.'."
print("Delete a quote run successfully.")

# # Verify that item "rock" does not exist
# r = requests.get(ENDPOINT + "?name=rock")
# assert r.status_code == 404

print("Test complete.")