import * as React from 'react';
import { View, Text } from 'react-native';
import { useEffect,useState } from 'react';
import axios from 'axios';

export default function HomeScreen({ navigation }) {
    const [stud,setStud]=useState([])
    const fitchD=()=>{
        axios.get('http://127.0.0.1:8000/Liststud')
        .then((res)=>setStud(res.data))
        .catch((err)=>console.log(err))
    } 
    const deleteStud=(id)=>{
        axios.delete(`http://127.0.0.1:8000/Delstud/${id}`)
        .then((res)=>alert('data is successfully deleted'),fitchD())
    }
    useEffect(()=>{fitchD()},[])
    return (
        
        <View style={{ flex: 1, alignItems: 'center', justifyContent: 'center' }}>
           {stud.map((studentinfo)=>{
               return ( 
               <Text
                onPress={() => navigation.navigate('Home')}
                style={{ fontSize: 50, fontWeight: 'bold' }}>

                    Student Name: {studentinfo.name}<br></br> 
                    
                    <button onClick={()=>deleteStud(studentinfo.id)}>Delete</button>
               </Text>)
           })}
        </View>
    );
}