# Trash-Classify

## Project Description
Upload a picture of a trash and it will help you determine what type of trash it is.

We have classified 8 different types of trash:
- General
- Plastic
- Food_Waste
- Waste_paper
- Glass
- Clothes (Textiles)
- Iron alumium
- Battery

## Try it!
### 1. Download the required files

```bash
git clone
```

### 2. Install Docker
Install docker by following the official documentation: https://docs.docker.com/engine/install/#supported-platforms.
> [!WARNING]
> You could use the convenience script below to install docker on Linux. However we recommend to not blindly download and execute scripts as sudo. But if you feel like it, you can of course use it. See below: 

<details>
    <summary>Using the convenience script</summary>

```bash
curl -fsSL https://get.docker.com | sudo sh
```

</details>

### 3. Start containers
```bash
docker compose up -d
```
> [!TIP]
> To change the port you want to use: \
> edit compose.yaml at line 23:
> ```yaml
> 22:     ports:
> 23:       - "your_custom_port:8000"
> ```

### 4. Run the app
Go to http://localhost:8000 (or your custom port) and view the website.

## Website Map

- Home: /
  * The home page where users can upload a picture
- About: /about
  * A poster about the project
- Display: /display
  * A pretty view of latest uploaded images and their predicted labels
  * Scroll down to view older images
  * In order to view display page, login is required and with staff status.\

- Admin Page: /admin
  * The admin page where you can see all uploaded details in the "His datas" section. 
  * (Only staff can access)


### Login credentials

We have created superuser and staff demo accounts both with staff status turned on.

| Account  | Password |
| -------- | -------- |
| admin    | admin    |
| staff    | staff    |
