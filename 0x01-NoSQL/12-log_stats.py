#!/usr/bin/env python3
""" log test"""
from pymongo import MongoClient

# Connect to the MongoDB server
client = MongoClient()
database = client["logs"]
collection = database["nginx"]

# Get the total number of documents in the collection
total_logs = collection.count_documents({})

print(f"{total_logs} logs")

# Get the number of documents with each HTTP method
http_methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
method_stats = {method: collection.count_documents({"method": method}) for method in http_methods}

print("Methods:")
for method, count in method_stats.items():
    print(f"    method {method}: {count}")

# Get the number of documents with method=GET and path=/status
get_status_count = collection.count_documents({"method": "GET", "path": "/status"})
print(f"{get_status_count} status check")

# Close the MongoDB connection
client.close()
