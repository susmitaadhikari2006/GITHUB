import 'package:flutter/material.dart';

void main() {
  runApp(const MyApp());
}
//MaterialApp
//Scaffold - create different screens
//AppBar
//Text - Title
//Futurte - ProgressBar
//Row
//checkBox/buttton for each row followed by text

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: "Senior To Do",
      theme: ThemeData(scaffoldBackgroundColor: Colors.white),
      home: MyHomePage(),
    );
  }
}

class MyHomePage extends StatelessWidget{
  Widget build(BuildContext context){
    return Scaffold(
      appBar: AppBar(
        title: Text("Senior To Do List"),
      ),
      body: Column(
        children:[
          Progress(),
          TaskList(),
        ]
      ),
    );
 }
}
class TaskItem extends StatefulWidget{
  final String label;
  const TaskItem({Key? key, required this.label}) : super(key:key);
  
  _TaskItemState createState() => _TaskItemState();
}
class _TaskItemState extends State<TaskItem>{
  bool? _value = false;
  Widget build(BuildContext context){
    return Row(
      children:[
        Checkbox(
        onChanged: (newValue) => setState(() => _value = newValue),
        value: _value
        ),
        Text(widget.label),
      ],
    );
  }
}

class TaskList extends StatelessWidget{
  Widget build(BuildContext context){
    return Column(
      children:[
        TaskItem(label:"Survive Flutter"),
        TaskItem(label:"Graduate"),
      ],
    );
  }
}

class Progress extends StatelessWidget{
  Widget build(BuildContext context){
    return Column(
      children:[
        Text("roeth is 10% far away from losing his sanity"),
        LinearProgressIndicator(value: .9),
      ],
    );
  }
}
