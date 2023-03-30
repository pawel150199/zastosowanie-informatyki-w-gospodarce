import React from  'react';
import * as Keycloak from  'keycloak-js';

let initOptions = {
    url: 'http://localhost:8080/auth/',
    realm: 'myrealmDemo',
    clientId: 'myReactClient',
    onload: 'login-required',
    KeycloakResponseType: 'code'
}

export var keycloak = Keycloak(initOptions);
keycloak.init({ onLoad: initOptions.onLoad, KeycloakResponseType: 'code' }).success((auth) => {
    if (!auth) {
        window.location.reload();
    } else {
        console.log("Authenticated");
    }
    setTimeout(() => {
        keycloak.updateToken(70).success((refreshed) => {
            if (refreshed) {
                console.debug('Token refreshed' + refreshed);
            } else {
                console.warn('Token not refreshed, valid for ' + Math.round(keycloak.tokenParsed.exp + keycloak.timeSkew - new Date().getTime() / 1000 + 'seconds'));
            }
        }).error(() => {
            console.error("Authenticated Failed!");
        });
        
    }, 60000)
});

const Login = () => {
    return (
        <>
        </>
    )
}

export default Login;