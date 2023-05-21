/* eslint-disable */
import React, { useState } from "react";
import { View, Text, TextInput, TouchableOpacity } from "react-native";
import { Button } from "react-bootstrap";
import { Link } from "react-router-dom";

import axios from "../../api/api"
import authHeader from "../../api/authHeader";

import styles from "./RegisterAdminStyle";

const RegisterAdmin = () => {
  // Team Admin
  const [firstName, setFirstName] = useState("");
  const [lastName, setLastName] = useState("");
  const [level, setLevel] = useState("");
  const [func, setFunc] = useState("");
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [confirmPassword, setConfirmPassword] = useState("");

  // Group
  const [name, setName] = useState("");
  const [number, setNumber] = useState("");
  const [szczep, setSzczep] = useState("");
  const [city, setCity] = useState("");
  const [groupId, setGroupId] = useState("");

  // Info
  // eslint-disable-next-line
  const [info, setInfo] = useState(" ");

  const handleRegisterAdmin = async () => {
    const group = "";
    const user = "";
    // Add group
    try {
      // eslint-disable-next-line
      group = await axios.post(
        "/groups",
        {
          name: name,
          number: number,
          szczep: szczep,
          city: city,
        },
        authHeader()
      );
      console.log("group.data: ", group.data);
      console.log("group.data.id: ", group.data.id);
      setGroupId(group.data.id);
    } catch (error) {
      console.error(error);
    }

    // Add teamadmin and add him to created group
    if (group.status === 200 || group.status === 201) {
      try {
        console.log("Group ID: ", groupId);
        if (password === confirmPassword) {
          // eslint-disable-next-line
          const user = await axios.post(
            "/users/admin/",
            {
              first_name: firstName,
              last_name: lastName,
              email: email,
              level: level,
              function: func,
              password: password,
              group_id: groupId,
              is_teamadmin: true
            },
            authHeader()
          );
        }
      } catch (error) {
        console.error(error);
      }
    }
    if (user.status === 201 || group.status === 201) {
      window.location.href = "/login";
    }
    if (user.status === 200  || user.status === 201 || group.status === 200 || group.status === 201) {
      setInfo("Drużynowy i grupa stworzono pomyślnie!");
    } else {
      setInfo("Wystąpił błąd!");
    }
  };

  return (
    <View style={styles.container}>
      <small>{info}</small>
      <br></br>
      <Text style={styles.title}>Załóż nową drużynę Harcerską</Text>
      <small>Jeśli twoja dryżyna jest już w aplikacji harcownik, poproś swojego drużynowego o dodanie :)</small>
      <br></br>
      <TextInput
        style={styles.input}
        placeholder="Nazwa Drużyny"
        value={name}
        onChangeText={setName}
      />
      <TextInput
        style={styles.input}
        placeholder="Numer drużyny"
        value={number}
        onChangeText={setNumber}
      />
      <TextInput
        style={styles.input}
        placeholder="Nazwa Szczepu Drużyny"
        value={szczep}
        onChangeText={setSzczep}
      />
      <TextInput
        style={styles.input}
        placeholder="Miasto Drużyny"
        value={city}
        onChangeText={setCity}
      />


      <br></br>
      <Text style={styles.title}>Załóż konto Drużynowego</Text>
      <small>Konto Drużynowego zostanie automatycznie zostanie dodane do drużyny</small>
      <br></br>
      <TextInput
        style={styles.input}
        placeholder="Imie"
        value={firstName}
        onChangeText={setFirstName}
      />
      <TextInput
        style={styles.input}
        placeholder="Nazwisko"
        value={lastName}
        onChangeText={setLastName}
      />
      <TextInput
        style={styles.input}
        placeholder="Poziom harcerza"
        value={level}
        onChangeText={setLevel}
      />
      <TextInput
        style={styles.input}
        placeholder="Funkcja harcerza"
        value={func}
        onChangeText={setFunc}
      />
      <TextInput
        style={styles.input}
        placeholder="Adres email"
        keyboardType="email-address"
        value={email}
        onChangeText={setEmail}
      />
      <TextInput
        style={styles.input}
        placeholder="Hasło"
        secureTextEntry={true}
        value={password}
        onChangeText={setPassword}
      />
      <TextInput
        style={styles.input}
        placeholder="Powtórz hasło"
        secureTextEntry={true}
        value={confirmPassword}
        onChangeText={setConfirmPassword}
      />
      {info && <p className="error">{info}</p>}
      <Button
        style={styles.button}
        onClick={handleRegisterAdmin}
      >
        Załóż konto Drużynowego
      </Button>
      <TouchableOpacity>
        <Link to="/login">
            <Text style={styles.link}>Masz już konto? Zaloguj się</Text>
        </Link>
      </TouchableOpacity>
      <br></br>
    </View>
  );
};

export default RegisterAdmin;
