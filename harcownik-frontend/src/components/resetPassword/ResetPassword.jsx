import React, { useState } from "react";
import { View, Text, TextInput, TouchableOpacity } from "react-native";

import axios from "../../api/api";
import { getLocalToken } from "../../api/utils";
import isLogged from "../../api/isLogged";

import styles from "./ResetPasswordStyle";
import authHeader from "../../api/authHeader";

const ResetPassword = () => {
  const [newPassword, setNewPassword] = useState("");
  const [newRepeatedPassword, setNewRepeatedPassword] = useState("");
  const [info, setInfo] = useState("");

  const handleResetPassword = async () => {
    const clearInputs = () => {
      setNewPassword("");
      setNewRepeatedPassword("");
    }

    try {
      if (isLogged()) {
        if (newPassword === newRepeatedPassword) {
          const response = await axios.post(
            "/reset-password",
            {
              token: getLocalToken("token"),
              new_password: newPassword,
            },
            authHeader()
          );
          clearInputs();
          if (response.status === 200 || response.status === 201) {
            window.location.href = "/user";
          }
        }
      }
    } catch (error) {
      console.error(error);
      setInfo("Password has not been succesfully changed! Please check data and try one more time.");
    }
  };

  return (
    <View style={styles.container}>
      <Text style={styles.title}>Reset Hasła</Text>
      <TextInput
        style={styles.input}
        placeholder="Nowe hasło"
        secureTextEntry={true}
        value={newPassword}
        onChangeText={setNewPassword}
      />
      <TextInput
        style={styles.input}
        placeholder="Powtórz nowe hasło"
        secureTextEntry={true}
        value={newRepeatedPassword}
        onChangeText={setNewRepeatedPassword}
      />
      {info && <p className="error">{info}</p>}
      <TouchableOpacity
        style={styles.button}
        onPress={handleResetPassword}
      >
        <Text>Zmień hasło</Text>
      </TouchableOpacity>
    </View>
  );
};

export default ResetPassword;
