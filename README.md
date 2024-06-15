# data-devops-realtime-financial-data

## Description

Ce projet implémente un pipeline complet de Data DevOps pour l'ingestion, le traitement, le stockage et la visualisation de données financières en temps réel à l'aide de l'API IEX Cloud.

## Structure du Projet

- **ingestion/** : Contient le script Python pour récupérer les données de l'API IEX Cloud et les envoyer à Kafka.
- **kafka/** : Contient les scripts et fichiers de configuration pour déployer Kafka sur Kubernetes.
- **processing/** : Contient le script PySpark pour le traitement de flux en temps réel.
- **cassandra/** : Contient le script CQL pour configurer la base de données Cassandra.
- **api/** : Contient le script Flask pour créer une API RESTful.
- **visualization/** : Contient les instructions pour configurer Grafana.
- **k8s/** : Contient les fichiers de configuration Helm et Terraform pour déployer les services sur Kubernetes.
- **scripts/** : Contient des scripts utilitaires pour déployer l'ensemble du pipeline.

## Configuration et Déploiement

### Prérequis

- Docker
- Kubernetes
- Helm
- Terraform
- Python 3.x

### Étapes de Déploiement

1. Cloner le dépôt :
    ```bash
    git clone https://github.com/Santoudllo/data-devops-realtime-financial-data.git
    cd data-devops-realtime-financial-data
    ```

2. Configurer et démarrer Kafka :
    ```bash
    cd kafka
    ./kafka-setup-k8s.sh
    ```

3. Déployer le producteur de données (ingestion) :
    ```bash
    cd ingestion
    docker build -t iex-producer .
    docker run -e API_KEY=your_iex_cloud_api_key iex-producer
    ```

4. Déployer le traitement de flux :
    ```bash
    cd processing
    docker build -t spark-stream-processor .
    docker run spark-stream-processor
    ```

5. Configurer Cassandra :
    ```bash
    cd cassandra
    docker build -t cassandra-setup .
    docker run cassandra-setup
    ```

6. Déployer l'API Flask :
    ```bash
    cd api
    docker build -t flask-api .
    docker run -p 5000:5000 flask-api
    ```

7. Configurer Grafana pour la visualisation :
    Suivre les instructions dans `visualization/grafana_setup.md`.

## Utilisation

- Accéder aux données via l'API RESTful : `http://localhost:5000/data`
- Visualiser les données en temps réel sur Grafana.

## Contribution

Les contributions sont les bienvenues. Veuillez soumettre une pull request ou ouvrir une issue pour toute suggestion ou amélioration.

## Licence

Ce projet est sous licence MIT.
