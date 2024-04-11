import 'package:flutter/material.dart';

void main() {
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      debugShowCheckedModeBanner: false,
      home: Scaffold(
          backgroundColor: Colors.yellow,
          body: Center(
            child: Stuff(),
          )),
    );
  }
}

class Stuff extends StatelessWidget {
  Widget build(BuildContext context) {
    return Column(
      mainAxisAlignment: MainAxisAlignment.center,
      children: <Widget>[
        Expanded(
          child: Center(
            child: Image.network(
              'https://codehs.com/uploads/c799accde67e1fd3bbd699119b4e1c83',
              height: 90.0,
              width: 90.0,
            ),
          ),
        ),
        Container(
          height: 100,
          color: Colors.red,
          alignment: Alignment.center,
          child: Text(
            'Log In',
            style: TextStyle(
              color: Colors.white,
              fontSize: 24,
              fontWeight: FontWeight.bold,
            ),
          ),
        ),
        Container(
          height: 100,
          color: Colors.blue,
          alignment: Alignment.center,
          child: Text(
            'Sign In',
            style: TextStyle(
              color: Colors.white,
              fontSize: 24,
              fontWeight: FontWeight.bold,
            ),
          ),
        ),
      ],
    );
  }
}
