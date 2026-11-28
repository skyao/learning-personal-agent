来源：https://support.google.com/gemini/answer/17094296?hl=en
取文：2026-11-28，直接下载（浏览器标识）

You can use skills to create and save custom instructions that can be used across your chats and tasks in Gemini Apps. Instead of re-typing your preferences or uploading the same files, Gemini can automatically use relevant skills or you can specify a skill to use for your task or workflow.

With skills, you can:

- **Save time and effort:** Build a skill once and use it in any chat or task thread.
- **Automate your workflow:** Gemini automatically recognizes when a skill is relevant to your current prompt and applies it for you.
- **Mix and match skills:** Use multiple skills for a single task to handle more complex work exactly the way you want. You can even use skills with other skills.

## What you need

To create and use skills, you must:

- **Be 18 or over.**
- **Sign in to the Gemini app**. [Learn how to sign in to Gemini Apps](https://support.google.com/gemini/answer/13278668).

**Important:**

- For now, skills are only available in the Gemini mobile app, the Gemini app on Mac, and the Gemini web app at [gemini.google.com](https://gemini.google.com).
- Skills work with [Keep Activity](https://myactivity.google.com/product/gemini) off, but features that require it, like Connected Apps, won't be available. For example, skills can’t access Google Workspace services like Google Calendar and Google Drive while Keep Activity is off.

## Create a skill

You can create a skill from a chat, task, or the Skills page. On the Skills page, you can create a skill with help from Gemini, build one from a prefilled or blank template, or upload a skill file or a folder with a `SKILL.md` file and optional supported reference files.

**Tip:** You can reference other skills within your skill instructions to build more complex workflows.

### Step 1: Go to the Skills page

1. On your computer, go to [gemini.google.com](https://gemini.google.com).
   - On a Mac, you can also open the Gemini app ![](images/img-01-4a5c21.png).
2. On the sidebar, click **Customize** ![](images/img-02-dc4a4e.png).
   - If you don’t find “Customize,” first click More ![](images/img-03-f0faa8.png).
3. At the top, click **Skills**.

### Step 2: Choose how you want to create a skill

Work with Gemini to create a skill

1. At the top of the Skills page, click **Create** ![and then](images/img-04-bfcdbc.png) **Create with Gemini** ![](images/img-05-99ea29.png).
2. Follow the instructions in the chat.

Edit a prefilled template to create a skill

1. On the Skills page under “Recommended,” click the skill template you want to use.
2. Make your edits to the name, description, and instructions.
3. Optionally, to add files to your skill, at the top, click **Add**. Then choose where to upload from:
   1. For files on your device, click **images** or **files**.
   2. For files in Google apps, click the source: **Google Drive** ![](images/img-06-196795.png), **Google Photos** ![](images/img-07-3854d6.png), or **Notebooks** ![Notebook](images/img-08-cd71d2.png).
   3. After adding your files, click **Upload**.
4. When you’re done, at the top, click **Create**.

**Tip:** To remove a file from your skill, find it below your skill instructions and click Remove ![](images/img-09-28961f.png).

Use a blank template to create a skill

1. At the top of the Skills page, click **Create** ![and then](images/img-04-bfcdbc.png) **Create manually** ![](images/img-10-75ae06.png).
2. Enter the name of your skill, a description of what it does, and instructions for it to follow.
3. Optionally, to add files to your skill, at the top, click **Add**. Then choose where to upload from:
   1. For files on your device, click **images** or **files**.
   2. For files in Google apps, click the source: **Google Drive** ![](images/img-06-196795.png), **Google Photos** ![](images/img-07-3854d6.png), or **Notebooks** ![Notebook](images/img-08-cd71d2.png).
   3. After adding your files, click **Upload**.
4. When you’re done, at the top, click **Create**.

**Tip:** To remove a file from your skill, find it below your skill instructions and click Remove ![](images/img-09-28961f.png).

Upload a file or folder to create a skill

**Important:** For now:

- Scripts that require access to the internet are not supported.
- You can add reference files to skills only by uploading them with your skill.

To create a skill from a file or folder upload:

1. At the top of the Skills page, click **Create** ![and then](images/img-04-bfcdbc.png) Upload ![](images/img-11-5a2bf9.png).
2. Select a `SKILL.md` file, or select a folder or `.zip` file that contains a `SKILL.md` file in its main folder.
   - If you upload a folder, it skips the option to add files individually.
3. Click **Open**.
4. Optionally, add files to your skill:
   - For files on your device, click **images** or **files**.
   - For files in Google apps, click the source: **Google Drive** ![](images/img-06-196795.png), **Google Photos** ![](images/img-07-3854d6.png), or **Notebooks** ![Notebook](images/img-08-cd71d2.png).
5. After you’re done adding your files, click **Upload**.
6. Review the skill and make any edits you want to make.
7. When you’re done, at the top, click **Create**.

### Upload requirements

#### Supported file types

You can upload plain-text based files. If you can open it in a basic text editor and read it, it is likely supported.

- **Supported:**
  - **Documents & text:** `.docx`, `.pdf`, `.rtf`, `.tex`, `.log`, `.md`, `.rst`, `.txt`, `.markdown`, `.odt`
  - **Spreadsheets & data tables:** `.csv`, `.ods`, `.xlsx`
  - **Presentations & slides:** `.odp`, `.pptx`
  - **Photos & images:** `.jpg`, `.png`, `.svg`, `.gif`, `.heic`, `.ico`, `.jpeg`, `.tif`, `.webp`
  - **Code & scripts:** `.py`, `.sh`, `.ipynb`, `.js`
  - **Web & UI files:** `.css`, `.html`, `.htm`
  - **Data & config:** `.env`, `.json`, `.toml`, `.xml`, `.yaml`, `.yml`
- **Not supported:**
  - **Legacy Microsoft Office:** `.doc`, `.xls`, `.ppt`
  - **Photos & images:** `.raw`
  - **Audio & video files**
  - **Archives & compressed files**
  - **Code & scripts:** `.cs`, `.kt`, `.kts`, `.php`, `.r`, `.rb`, `.scala`, `.swift`, `.ts`
  - **Web & UI files:** `.jsx`, `.tsx`
  - **Data & config:** `.sql`

#### Structure & naming

- **Skill metadata:** Your project must include a `SKILL.md` file located in the root (main) folder.
- **Naming convention:** The skill name inside `SKILL.md` must use all lowercase with words separated by a hyphen (such as `my-new-skill`).
- **Size limit:** The total size of all uploaded files must not exceed 100 MB.

#### Security restrictions

- **No external actions:** Scripts can’t perform actions or requests on external websites.

**Tip:** Before you upload, check for hidden binary files (like `.DS_Store` or `.pyc`) that might cause the upload to fail.

Ask Gemini to create a skill in a chat

1. On your computer, go to [gemini.google.com](https://gemini.google.com).
2. In the text box, ask Gemini to create a skill and describe what you want the skill to do.
   - For example, `Create a skill based on these instructions:` <your instructions>.
3. Click Submit ![](images/img-12-c4d89f.png). Gemini will create your skill and save it to your Skills page.
4. To make edits to the skill, just describe your edits in the chat.

**Tip:** You can’t activate, deactivate, or delete a skill from a chat or task thread. To perform those actions, on the sidebar, click **Customize** ![](images/img-02-dc4a4e.png) ![and then](images/img-04-bfcdbc.png) **Skills**.

## Explore skill examples

Skills can automate a wide range of tasks and workflows:

- **Writing help:** A skill can help with coursework and have specific instructions not to give answers. It can include your past papers, feedback, and scores.
- **Brainstorming:** A skill can expand on ideas and then generate a design document based on a standard template.
- **Tactical support:** A skill can help with specific tasks, like converting bank statements into formatted spreadsheets or generating product descriptions for a website.
- **Career guidance:** A skill can give advice on job opportunities based on your resume.

## Use skills for a task

Skills are designed to work in the background and can be used across Gemini chats and tasks. You can ask Gemini to use specific skills for a task. Gemini can also automatically use a skill when it’s relevant to your task.

- **Ask Gemini to use a skill:** In the chat or task thread, enter `/` (or `@`, if you have the updated shortcut), then select the skill.
- **Gemini automatically uses skills:** Gemini can automatically use activated skills based on the context and intent of your task.
- **Combine skills:** You can include multiple skills for Gemini to use in a single task. This helps Gemini complete complex, multi-step tasks effectively.

## Manage your skills

You can manage your skills from the Skills page.

Manage Gemini’s automatic use of a skill

Gemini can only automatically use skills that are turned on. You can turn skills off at any time. If a skill is off and you ask Gemini to use it, Gemini will ask you if you want to turn it back on.

**To stop Gemini from using a skill automatically:**

1. On your computer, go to [gemini.google.com](https://gemini.google.com).
   - On a Mac, you can also open the Gemini app ![](images/img-01-4a5c21.png).
2. On the sidebar, click **Customize** ![](images/img-02-dc4a4e.png).
   - If you don’t find “Customize,” first click More ![](images/img-03-f0faa8.png).
3. At the top, click **Skills**.
4. Click the skill that you want Gemini to stop using.
5. At the top, click More ![](images/img-03-f0faa8.png) ![and then](images/img-04-bfcdbc.png) **Deactivate** ![](images/img-13-c96774.png).

**To allow Gemini to automatically use a skill again**, follow the same steps and click **Activate** ![](images/img-14-0ea28f.png).

Edit a skill

**Important:** To update files in a skill, you need to upload the entire skill with its reference files again.

1. On your computer, go to [gemini.google.com](https://gemini.google.com).
   - On a Mac, you can also open the Gemini app ![](images/img-01-4a5c21.png).
2. On the sidebar, click **Customize** ![](images/img-02-dc4a4e.png).
   - If you don’t find “Customize,” first click More ![](images/img-03-f0faa8.png).
3. At the top, click **Skills**.
4. Click the skill you want to edit.
5. Make your edits.
   - To edit directly, update the "Description" and "Instructions" fields.
   - To edit conversationally, click More ![](images/img-03-f0faa8.png) ![and then](images/img-04-bfcdbc.png) **Edit with Gemini** ![](images/img-15-9ea990.png).
   - To upload a file to replace a skill, click More ![](images/img-03-f0faa8.png) ![and then](images/img-04-bfcdbc.png) **Replace skill** ![](images/img-11-5a2bf9.png).
6. Manage files in your skill:
   - To add a file, click **Add files**.
   - To remove a file, find it below your skill instructions and click Remove ![](images/img-09-28961f.png).
   - To replace a file, click More ![](images/img-03-f0faa8.png) ![and then](images/img-04-bfcdbc.png) **Replace file** ![](images/img-16-c6f183.png).
7. When you’re done, at the top, click **Save**.

**Tip:** You can also ask Gemini to update a skill and its files.

Delete a skill

**Important:** If you delete a skill, it can’t be undone.

You can only delete a skill from the Skills page.

1. On your computer, go to [gemini.google.com](https://gemini.google.com).
   - On a Mac, you can also open the Gemini app ![](images/img-01-4a5c21.png).
2. On the sidebar, click **Customize** ![](images/img-02-dc4a4e.png).
   - If you don’t find “Customize,” first click More ![](images/img-03-f0faa8.png).
3. At the top, click **Skills**.
4. Hover over the skill you want to delete.
5. Click More ![](images/img-03-f0faa8.png) ![and then](images/img-04-bfcdbc.png) **Delete** ![](images/img-17-23ae4d.png).

Download a skill

1. On your computer, go to [gemini.google.com](https://gemini.google.com).
   - On a Mac, you can also open the Gemini app ![](images/img-01-4a5c21.png).
2. On the sidebar, click **Customize** ![](images/img-02-dc4a4e.png).
   - If you don’t find “Customize,” first click More ![](images/img-03-f0faa8.png).
3. At the top, click **Skills**.
4. Hover over the skill you want to download.
5. Click More ![](images/img-03-f0faa8.png) ![and then](images/img-04-bfcdbc.png) **Download** ![](images/img-18-cd655c.png). This downloads your skill in a `.zip` file.
   - Any Google Drive files and notebooks in your skill aren't included in the download to maintain their live, real-time connection.

## Share skills & manage access

**Important:**

- For now, you can only share and manage access to skills in the Gemini web app at [gemini.google.com](https://gemini.google.com).
- A skill can only be shared by its owner and individuals with Editor access.
- For now, skills with a notebook attached can't be shared.

Share a skill

**Important:** If your skill includes files, you’ll also need to share access to those files.

1. On your computer, go to [gemini.google.com](https://gemini.google.com).
2. On the sidebar, click **Customize** ![](images/img-02-dc4a4e.png) ![and then](images/img-04-bfcdbc.png) **Skills**.
3. Hover over the skill you want to share.
4. Click More ![](images/img-03-f0faa8.png) ![and then](images/img-04-bfcdbc.png) **Share skill** ![](images/img-19-c4fa6e.png). This creates a copy of the skill in Google Drive.
5. Enter the email address you want to share with.
   - If you use a [work or school account](https://support.google.com/accounts/answer/6250166), you can share with suggested recipients.
6. Select their access level: **Viewer** or **Editor**.
7. Optionally:
   - To set an access expiration date, click the access level ![and then](images/img-04-bfcdbc.png) **Add expiration**. Then next to the expiration date, click Edit expiration ![](images/img-20-01c8d6.png).
   - To skip sending a notification email, uncheck **Notify people**.
   - To include a message in the notification email, enter it in the text box.
8. Click **Send**.

**Tip:** You can share a skill from its details page. At the top, click More ![](images/img-03-f0faa8.png) ![and then](images/img-04-bfcdbc.png) **Share skill**.

#### About access levels

- Editors can:
  - Share the skill with others
  - Make changes to the skill’s instructions and uploaded files
- Viewers can:
  - Use the shared skill
  - View the skill’s description, instructions, and uploaded files

Add a shared skill

When the owner shares a skill with you, it’s added as inactive under “All” on your Skills page. You also get an email notification if the owner chose to notify you.

1. Go to the email about the shared skill.
2. Click **Open** to open the skill in Gemini.
3. At the top, click **Add skill**.
   - This adds the skill to your Skills page with a Shared icon ![](images/img-21-3bf806.png).
   - You can use a shared skill in a chat by entering `@` and selecting it.
   - Gemini can automatically use active shared skills when they’re relevant.
   - If you have a skill with the same name, you can:
     - Choose to save a copy. Copies don’t automatically sync when the original skill is updated.
     - Change the name if you have edit access, or ask the owner to change it if you don’t. This changes the name for everyone with access.

**Tip:** After you add a skill with "Viewer" access, you can request edit access. On the Skills page, click the skill, and at the top, click **Request edit access**.

Remove someone’s access to a shared skill

1. On your computer, go to [gemini.google.com](https://gemini.google.com).
2. On the sidebar, click **Customize** ![](images/img-02-dc4a4e.png) ![and then](images/img-04-bfcdbc.png) **Skills**.
3. Hover over the skill you want to remove access to.
4. Click More ![](images/img-03-f0faa8.png) ![and then](images/img-04-bfcdbc.png) **Share skill** ![](images/img-19-c4fa6e.png).
5. Next to the individual’s name, click **Viewer** or **Editor** ![and then](images/img-04-bfcdbc.png) **Remove access**.
6. Click **Save**.

Transfer ownership of a shared skill

As the owner of a skill, you can transfer ownership to anyone that it’s been shared with. If you haven’t already, first [share the skill](#share_skill) with the new owner. Then, transfer ownership.

1. On your computer, go to [gemini.google.com](https://gemini.google.com).
2. On the sidebar, click **Customize** ![](images/img-02-dc4a4e.png) ![and then](images/img-04-bfcdbc.png) **Skills**.
3. Hover over the skill you want to transfer ownership for.
4. Click More ![](images/img-03-f0faa8.png) ![and then](images/img-04-bfcdbc.png) **Share skill** ![](images/img-19-c4fa6e.png).
5. Next to the new owner’s name, click **Viewer** or **Editor** ![and then](images/img-04-bfcdbc.png) **Transfer ownership**.

Delete or remove a shared skill

**Important:** If you delete a shared skill as the owner, it's permanently removed for everyone. If you aren't the owner, deletion of a skill removes it for you only.

1. On your computer, go to [gemini.google.com](https://gemini.google.com).
2. On the sidebar, click **Customize** ![](images/img-02-dc4a4e.png) ![and then](images/img-04-bfcdbc.png) **Skills**.
3. Click the skill you want to delete or remove.
4. At the top, click More ![](images/img-03-f0faa8.png) ![and then](images/img-04-bfcdbc.png) **Delete** ![](images/img-17-23ae4d.png).

**Tip:** To keep a skill for later, deactivate it instead. If you deactivate a shared skill, it only affects you. Others can still use and update it.

## Common questions

What's the difference between a task, schedule, and skill?

To help you get the most out of tasks, it’s helpful to understand the three building blocks that power its logic: tasks, schedules, and skills. Think of these as the what, when, and how.

**A task is your high-level goal.** It represents a complete project or objective you want Gemini to manage for you.

- **Example:** "Plan and manage my business trip to London."

**A schedule lets you hand over tasks** to Gemini so they run automatically in the background. You tell Gemini what to do and when to do it. Tasks can be scheduled to run at a specific date and time or in response to an event.

- **Example:** "Every day at 8AM (condition), give me an update on AI news (task)"
- **Example:** "When my flight is delayed (condition), notify me and propose an update to my itinerary (task)."

**Tip:** Schedules for tasks are different from scheduled actions in Gemini chat. [Learn how to schedule actions in Gemini Apps](https://support.google.com/gemini/answer/16316416).

**A skill is a set of reusable instructions and additional context.** It teaches Gemini how to do a specific task and what tools to use. You can specify the skill Gemini should use for a task or a schedule’s action. Gemini can also automatically use a skill when it’s relevant to a task.

- **Example:** Using a "Travel Booking" skill and a "Gmail Writing" skill simultaneously to rebook a room and send a confirmation.

In summary, you define the task (what you want), set the schedules (when it should happen), and provide the skills (how to do it) to complete the work.

How do I recreate my Gems as skills?

When we remove Gems, we’ll automatically recreate your Gems as skills. If you want to start using your Gems as skills earlier, you can manually recreate them. [Learn how to recreate your Gems as skills](https://support.google.com/gemini/answer/18560919#gem_to_skill).

## Related resources

- [Manage your tasks & workflows in Gemini Apps](https://support.google.com/gemini/answer/17094507)
- [Write effective skills for Gemini Apps](https://support.google.com/gemini/answer/17102773)
