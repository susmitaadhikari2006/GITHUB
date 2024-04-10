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
          )
      ),
    );
  }
}

class Stuff extends StatelessWidget{
  Widget build(BuildContext context){
    return Column(
            mainAxisAlignment:MainAxisAlignment.center,
            children: <Widget>[
              Image.network(
                'https://codehs.com/uploads/c799accde67e1fd3bbd699119b4e1c83',
                height: 90.0,
                width: 90.0,
              ),
              ElevatedButton(
                child: Text('LOG IN',
                    style: TextStyle(color: Colors.white, fontSize: 20)),
                style: ElevatedButton.styleFrom(
                  backgroundColor: Colors.red,
                  elevation: 0,
                ),
                onPressed: () {},
              ),
              ElevatedButton(
                child: Text("SIGN UP",
                    style: TextStyle(color: Colors.white, fontSize: 20)),
                style: ElevatedButton.styleFrom(
                  backgroundColor: Colors.blueAccent,
                  elevation: 0,
                ),
                onPressed: () {},
              ),
            ],
          );
  }
}
