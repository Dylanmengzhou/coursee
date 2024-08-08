#!/bin/sh
# Create a folder (named dmg) to prepare our DMG in (if it doesn't already exist).
mkdir -p dist/dmg
# Empty the dmg folder.
rm -r dist/dmg/*
# Copy the app bundle to the dmg folder.
cp -r "dist/Coursee.app" dist/dmg
# If the DMG already exists, delete it.
test -f "dist/Coursee.dmg" && rm "dist/Coursee.dmg"
create-dmg \
  --volname "Coursee" \
  --volicon "Hello World.icns" \
  --window-pos 200 120 \
  --window-size 600 300 \
  --icon-size 100 \
  --icon "Coursee.app" 175 100 \
  --hide-extension "Coursee.app" \
  --app-drop-link 425 120 \
  "dist/Coursee.dmg" \
  "dist/dmg/"