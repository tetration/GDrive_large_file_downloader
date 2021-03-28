# This is a modified version of nsadawi's Download-Large-File-From-Google-Drive-Using-Python

Link to  [nsadawi's vanilla code](https://github.com/nsadawi/Download-Large-File-From-Google-Drive-Using-Python)
I've adapted his code to accept Argument Parsers. This way all you need to do now when running his script is to type the file ID and final destination directly when running the script.
Example:
> python .\downloadGfile.py 3dasdp343343dswww43 C:\Git\test\mytext.txt

And Voilà! You no longer need to modify this python script each time you want to download a different document or put it in a different destination. All you have to do now is write the the ID and the final destination of each file you want to download from Google Drive

## Warning: 
All the files you want to dowload from Google Drive still need to be set to public otherwise this script wont be able to download them at all!

## How to use it

- In order to download the file stored in Google Drive all you need to do now when running his script is to type it in your commandline the following way: 

python  downloadGfile.py **GFileLink** **Destination**

Example:
 `python .\downloadGfile.py 3dasdp34ThisIsAFakeID3343dswww43`

## Finding out the ID of a Google Drive File

**Google Drive File ID** is a unique identifier of the **file** on **Google Drive**. **File IDs** normally, they are stable throughout the lifespan of the **file**, even if the **file** name changes. To find out the id of the **File ID**, you wish to download  right-click on the name of the **file**, then choose the Get Shareable Link option, and turn on Link Sharing if needed. A modal will **popup** with a link looking similar to this
> https://drive.google.com/file/d/THIS_IS_WHERE_THE_ID_WILL_BE _LOCATED/view?usp=sharing

As shown above all you will have to do now is copy the **THIS_IS_WHERE_THE_ID_WILL_BE _LOCATED** and paste it combined with the final destination of the file you wish to download from Google Drive. Obviously, each file in your Google Drive will have a unique ID.
