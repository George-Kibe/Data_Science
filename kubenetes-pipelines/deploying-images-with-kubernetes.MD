### 1.Creating all docker images at once using bash command
```bash 01_build_and_upload_images.sh```
### 2. Creating all pods from different manifests at once
```bash 02_apply_manifests.sh```

### 3. Get logs of a given pod  kubectl logs <pod-name>
``` kubectl logs pod-list-files```

## Other Useful commands
1. Delete all pods
```kubectl delete pods --all```
2. Checking if a .csv is valid. You can alternatively check using vscode extension. Output is 19
```awk -F',' '{print NF}' yellow_tripdata_2024-01.partial.csv | sort -nu```