for f in *.day; do 
    mv -- "$f" "${f%.day}.toml"
done
