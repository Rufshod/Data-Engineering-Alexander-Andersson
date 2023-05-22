#!/bin/bash

cd pokemons

while read -r line
do
     echo -e "Downloading data for pokemon $line"
     curl https://pokeapi.co/api/v2/pokemon-species/$line > "${line}.json"
     sleep 2
     echo -e "Download complete for pokemon $line"
     sleep 1
done < pokemon_list.txt

