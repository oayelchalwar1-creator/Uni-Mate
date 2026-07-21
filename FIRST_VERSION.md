# UniMate: first working version

Follow the steps in this order. Do not add AI, APIs, or databases yet.

## Part A: Create the Alexa skill

1. Go to the Alexa Developer Console and select **Create Skill**.
2. Enter **UniMate** as the skill name.
3. Choose **Custom** and **Alexa-Hosted: No**.
4. Choose **Start from scratch**, then create the skill.
5. Under **Build**, open **JSON Editor**.
6. Delete everything in the editor.
7. Open `docs/alexa-interaction-model.json` in this folder, copy all of its contents, paste it into the JSON Editor, and select **Build Model**.

## Part B: Create the Lambda backend

1. In AWS, choose the **London** region (`eu-west-2`) so it matches the Alexa skill endpoint region.
2. Open Lambda and select **Create function**.
3. Choose **Author from scratch**.
4. Function name: `unimate-alexa-backend`.
5. Runtime: **Python 3.12**.
6. Select **Create function**.
7. In the `lambda_function.py` code editor, delete all existing text.
8. Copy all text from `COPY_PASTE_LAMBDA.py` and paste it into the editor.
9. Select **Deploy**.
10. In Lambda, select **Add trigger**. Choose **Alexa Skills Kit**, then select your UniMate skill and confirm.

## Part C: Connect and test

1. Return to the Alexa Developer Console.
2. Select **Endpoint**.
3. Choose **AWS Lambda ARN** and paste the ARN shown at the top-right of your Lambda function page.
4. Save endpoints.
5. Open the **Test** tab and enable testing for Development.
6. Test these exact messages:
   - `open uni mate`
   - `explain cloud computing`
   - `quiz me on machine learning`

## If something fails

Take a screenshot of the red error message and the Lambda CloudWatch log entry. Do not alter code at random; send the screenshot so the specific configuration issue can be corrected.
