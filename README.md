# SITYKE
Send It To Your Kindle Efficiently

---

开发这个软件的初衷起源于一节地理课后。

我想要把老师的所有PPT全部导入到我的**kindle**中，可是由于kindle只能读取```.pdf```格式的文件，所以我只能用**PowerPoint**一个一个地转换。

**那岂不是要累死我？**

于是就有了开发**SITYKE**的想法。

这个程序自动扫描当前文件夹下的所有文件，找出其中的**PowerPoint演示文稿**并将其转化为```.pdf```。

（后来考虑到可能还有Word版本的资料就也加了**Word文档**转换为```.pdf```的功能）

---

用法：

将需要转换的文件放到sityke文件夹下，在cmd中输入

```
python sityke.py
```

支持```.ppt``` ```.pptx``` ```.doc``` ```.docx```转换成```.pdf```并自动导入kindle