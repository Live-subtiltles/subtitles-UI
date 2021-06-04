import 'package:flutter/material.dart';
import 'package:avatar_glow/avatar_glow.dart';

void main() => runApp(MyApp());

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      routes: {
        '/': (context) => HomePage(),
      },
    );
  }
}

class HomePage extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
        appBar: AppBar(
          title:
              Image.asset('images/logo.png', fit: BoxFit.contain, height: 60),
          centerTitle: false,
          toolbarHeight: 100,
          backgroundColor: Colors.grey[200],
          shadowColor: Colors.transparent,
          actions: <Widget>[
            Row(children: <Widget>[
              Column(children: <Widget>[
                Expanded(
                  child: Container(),
                  flex: 1,
                ),
                Expanded(
                    child: Image.asset('images/Untitled-1.png',
                        fit: BoxFit.contain),
                    flex: 10),
                Expanded(
                  child: Container(),
                  flex: 1,
                ),
              ]),
              SizedBox(width: 10)
            ])
          ],
        ),
        backgroundColor: Colors.grey[200],
        body: Row(
            // crossAxisAlignment: CrossAxisAlignment.stretch,
            // mainAxisAlignment: MainAxisAlignment.spaceEvenly,
            children: <Widget>[
              Expanded(flex: 1, child: Container()),
              Expanded(
                  flex: 6,
                  child: Container(
                    child: Column(
                      crossAxisAlignment: CrossAxisAlignment.start,
                      mainAxisAlignment: MainAxisAlignment.center,
                      children: <Widget>[
                        Expanded(child: Container(), flex: 3),
                        Expanded(
                            flex: 8,
                            child: FittedBox(
                              fit: BoxFit.contain,
                              child: Text(
                                "LIVE \nSUBTITLES",
                                style: TextStyle(
                                  fontWeight: FontWeight.w800,
                                ),
                              ),
                            )),
                        Expanded(
                            flex: 1,
                            child: FittedBox(
                                fit: BoxFit.contain,
                                child: Text("Powered by DeepSpeech",
                                    style: TextStyle(
                                        fontWeight: FontWeight.w100,
                                        height: 0.9,
                                        fontStyle: FontStyle.italic)))),
                        Expanded(child: Container(), flex: 4),
                      ],
                    ),
                    padding: EdgeInsets.all(30.0),
                  )),
              // Expanded(child: Container(), flex: 1),
              Expanded(
                  flex: 3,
                  child: Container(
                    child: Column(
                      crossAxisAlignment: CrossAxisAlignment.center,
                      mainAxisAlignment: MainAxisAlignment.center,
                      children: <Widget>[
                        Expanded(child: Container(), flex: 3),
                        Expanded(
                            flex: 2,
                            child: FittedBox(
                                fit: BoxFit.fill,
                                child: IconButton(
                                  icon: Icon(Icons.chevron_right),
                                  onPressed: () {
                                    Navigator.push(
                                      context,
                                      MaterialPageRoute(
                                          builder: (context) =>
                                              RecordingPage()),
                                    );
                                  },
                                ))),
                        Expanded(
                            flex: 1,
                            child: FittedBox(
                                fit: BoxFit.contain,
                                child: Text("Get \nstarted!",
                                    textAlign: TextAlign.center,
                                    style: TextStyle(
                                      fontSize: 18,
                                      fontWeight: FontWeight.w300,
                                    )))),
                        Expanded(child: Container(), flex: 4),
                      ],
                    ),
                    padding: EdgeInsets.all(30),
                  )),
              Expanded(
                flex: 1,
                child: Container(),
              )
            ]));
  }
}

class RecordingPage extends StatefulWidget {
  @override
  _RecordingPageState createState() => _RecordingPageState();
}

class _RecordingPageState extends State<RecordingPage> {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Image.asset('images/logo.png', fit: BoxFit.contain, height: 60),
        centerTitle: false,
        toolbarHeight: 100,
        backgroundColor: Colors.grey[200],
        shadowColor: Colors.transparent,
        actions: <Widget>[
          Row(children: <Widget>[
            Column(children: <Widget>[
              Expanded(
                child: Container(),
                flex: 1,
              ),
              Expanded(
                  child:
                      Image.asset('images/Untitled-1.png', fit: BoxFit.contain),
                  flex: 10),
              Expanded(
                child: Container(),
                flex: 1,
              ),
            ]),
            SizedBox(width: 10)
          ])
        ],
      ),
      body: Row(
        crossAxisAlignment: CrossAxisAlignment.stretch,
        mainAxisAlignment: MainAxisAlignment.spaceEvenly,
        children: <Widget>[
          Expanded(
              flex: 1,
              child: Container(
                color: Colors.transparent,
              )),
          Expanded(
              flex: 6,
              child: Column(children: <Widget>[
                Expanded(
                    flex: 2,
                    child: Container(
                      color: Colors.transparent,
                    )),
                Expanded(
                  flex: 10,
                  child: Container(
                    decoration:
                        BoxDecoration(border: Border.all(color: Colors.black)),
                    child: SingleChildScrollView(
                        reverse: true,
                        child: Container(
                            child: Align(
                                alignment: Alignment.center,
                                child: Container(
                                    height: 450,
                                    padding: EdgeInsets.all(15),
                                    alignment: Alignment.center,
                                    child: Text(
                                      "the transcription goes here ......................................................................................................................................"
                                      "\n........"
                                      "\n........."
                                      "\n........."
                                      "\n........."
                                      "\n........."
                                      "\n........."
                                      "\n........."
                                      "\n........."
                                      "\n........."
                                      "\n........."
                                      "\n........."
                                      "\n........."
                                      "\n........."
                                      "\n........."
                                      "\n........."
                                      "\n........."
                                      "\n.........",
                                      textAlign: TextAlign.left,
                                      style: TextStyle(
                                        fontSize: 20,
                                        height: 1.5,
                                      ),
                                    ))))),
                  ),
                ),
                Container(
                  height: 85,
                  child: FavoriteWidget(),
                )
              ])),
          Expanded(
            flex: 1,
            child: Container(color: Colors.transparent),
          )
        ],
      ),
    );
  }
}

class FavoriteWidget extends StatefulWidget {
  @override
  _FavoriteWidgetState createState() => _FavoriteWidgetState();
}

class _FavoriteWidgetState extends State<FavoriteWidget> {
  bool isrecording = false;

  void _togglerecording() {
    setState(() {
      if (isrecording) {
        isrecording = false;
      } else {
        isrecording = true;
      }
    });
  }

  @override
  Widget build(BuildContext context) {
    return Row(
      mainAxisSize: MainAxisSize.min,
      children: [
        Container(
            height: 100,
            child: Align(
                alignment: Alignment.center,
                child: AvatarGlow(
                  animate: isrecording,
                  glowColor: Colors.redAccent,
                  duration: const Duration(milliseconds: 1500),
                  repeatPauseDuration: const Duration(milliseconds: 75),
                  repeat: true,
                  showTwoGlows: false,
                  endRadius: 35.0,
                  child: IconButton(
                    icon:
                        (isrecording ? Icon(Icons.mic) : Icon(Icons.mic_none)),
                    iconSize: 50,
                    onPressed: _togglerecording,
                  ),
                )))
      ],
    );
  }
}
