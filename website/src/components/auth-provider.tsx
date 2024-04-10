import { UserAuthenticate } from "@/types/auth";
import { ReactNode, createContext, useEffect, useState } from "react";

export interface AuthContextType {
  username: string;
  token: string;
  email: string;
  loading: boolean;
  onLogin: ({ username, password }: UserAuthenticate) => void;
  onRegister: ({ username, email, password }: UserAuthenticate) => void;
}

const AuthContext = createContext<AuthContextType>(null!);

export const AuthProvider = ({ children }: { children: ReactNode }) => {
  const [username, setUsername] = useState("");
  const [email, setEmail] = useState("");
  const [token, setToken] = useState("");
  const [loading, setLoadign] = useState(false);

  useEffect(() => {
    retriveToken();
  }, []);

  const retriveToken = () => {};

  const handleLogin = async ({ username, password }: UserAuthenticate) => {};

  const handleRegister = async ({
    username,
    email,
    password,
  }: UserAuthenticate) => {};

  const auth: AuthContextType = {
    username,
    email,
    token,
    loading,
    onLogin: handleLogin,
    onRegister: handleRegister,
  };

  return <AuthContext.Provider value={auth}></AuthContext.Provider>;
};
