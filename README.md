# Project Name

## Overview

This project handles recursive file operations (searching for images in directories), manages errors related to corrupted image files, and stores image file paths in a MongoDB database. It is designed with a flexible interface and integrates with MongoDB using `pymongo`.

## Features
- Recursively search for images (PNG, JPG, JPEG) in a directory.
- Handle errors related to corrupted image files.
- Store file paths in a MongoDB database.
- Use environment variables to configure MongoDB connection.

## Prerequisites

- **Python 3.8+**
- **MongoDB**: You must have MongoDB installed on your system. Follow the installation guide below to set it up.

### MongoDB Installation

1. **Install MongoDB**  
   Follow the official MongoDB installation guide for your operating system:  
   [MongoDB Installation Docs](https://docs.mongodb.com/manual/installation/)

2. **Start MongoDB**  
   Once installed, you can start the MongoDB server with the following command:
   
   ```bash
   mongod --dbpath /path/to/your/db
