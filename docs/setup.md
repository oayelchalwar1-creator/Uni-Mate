# UniMate Foundation Setup

## Purpose

This document records how the first prototype was deployed. Update it as you work;
it will provide evidence for the implementation chapter.

## AWS Lambda

1. Create a Python 3.12 Lambda function named `unimate-alexa-backend`.
2. Upload the files from `backend/` as a ZIP, with the Python files at the ZIP root.
3. Set the handler to `lambda_function.lambda_handler`.
4. Add an Alexa Skills Kit trigger and select the UniMate skill.
5. Test the LaunchRequest before testing custom intents.

## Important security rule

Do not commit passwords, AWS access keys, API keys, or personal user data.
