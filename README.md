# fetch my tweeets!

## Description

The **fetch my tweeets!** GitHub Action fetches your recent tweets without much hassle and updates your GitHub profile README with the latest content. This action allows you to showcase your recent tweets directly in your profile.

## Inputs

#### `twitter_username`

- **Description**: Twitter username to fetch tweets from.
- **Required**: `true`
- **Example**: `john_doe`

#### `email_token`

- **Description**: Twitter email for authentication.
- **Required**: `true`
- **Example**: `john_doe@example.com`

#### `password_token`

- **Description**: Twitter password for authentication.
- **Required**: `true`
- **Example**: `your_password`

#### `github_token`

- **Description**: GitHub token for authentication to update the profile README.
- **Required**: `true`
- **Example**: `ghp_XXXXXXXXXXXXXXXXXXXXXX`

## Usage

To use the **fetch my tweets!** action, create a workflow in your GitHub repository. Follow these steps:

1. **Create a Workflow File**

   In your repository, create a file named `.github/workflows/fetch-tweeets.yml`.

2. **Add the Workflow Configuration**

   Add the following configuration to the file:

  ```yaml
   name: Update Profile README

	on:
	  schedule:
	    - cron: '0 0 * * *'  # Runs daily at midnight
	  workflow_dispatch: # Allows manual triggering

	jobs:
	  update-readme:
	    runs-on: ubuntu-latest
	    steps:
	      - name: Checkout repository
	        uses: actions/checkout@v3

	      - name: Update README with latest articles
	        uses: krrishmahar/fetch-tweeets!@v1.0.0
	        with:
	          username: john_doe
			  tweet_limit: 4
			  email_token: john_doe@example.com
			  password_token: ${{ secrets.password_token }}
			  github_token: ${{ secrets.TOKEN_GITHUB }}
	```


### Configure Secrets for fetch my tweets!

To use the **fetch tweeets!** GitHub Action, you must configure your Twitter credentials and GitHub personal access token as secrets in your repository. Follow these steps to add the required secrets:

#### Go to Your Repository Settings

- Navigate to your repository on GitHub.
- Click on **Settings**.

#### Access Secrets Management

- In the left sidebar, click on **Secrets and variables**.
- Then select **Actions**.

#### Add New Secrets

- Click on **New repository secret**.
- Name the secrets `TWITTER_USERNAME`, `TWITTER_EMAIL`, `TWITTER_PASSWORD`, and `GITHUB_TOKEN`.
- Paste the corresponding values for each secret.
- Click **Add secret** to save.

After adding the secrets, your GitHub Action can authenticate and update your profile README with the latest tweets.

---
### Insert Tweet Tags in README.md

In your `README.md` file, add the following tags where you want the tweets to appear:

```markdown
<!-- TWEETS -->

<!-- /TWEETS -->
```