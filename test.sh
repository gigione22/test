IFS=':' read -ra dirs <<< "$PATH"
for d in "${dirs[@]}"; do
    if [ -d "$d" ]; then
        count=$(find "$d" -maxdepth 1 -type f -perm +111 2>/dev/null | wc -l)
        echo "$d: $count executables"
    else
        echo "$d: (missing directory)"
    fi
done

