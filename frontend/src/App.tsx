import "./styles/main.css";
import { FC, Suspense, lazy } from "react";
import { QueryClientProvider } from "react-query";
import { ChakraProvider } from "@chakra-ui/react";
import { BrowserRouter, Route, Routes } from "react-router-dom";
import queryClient from "./lib/queryClient";
import Fallback from "./components/Fallback";

const LandingPage = lazy(() => import("./pages/LandingPage"));
const DashboardPage = lazy(() => import("./pages/DashboardPage"));
const RegisterPage = lazy(() => import("./pages/RegisterPage"));
const LoginPage = lazy(() => import("./pages/LoginPage"));
const NotFoundPage = lazy(() => import("./pages/NotFoundPage"));

const App: FC = () => {
    return (
        <ChakraProvider>
            <QueryClientProvider client={queryClient}>
                <Suspense fallback={<Fallback />}>
                    <BrowserRouter>
                        <Routes>
                            <Route index element={<LandingPage />} />
                            <Route path="/dash" element={<DashboardPage />} />
                            <Route path="/register" element={<RegisterPage />} />
                            <Route path="/login" element={<LoginPage />} />
                            <Route path="*" element={<NotFoundPage />} />
                        </Routes>
                    </BrowserRouter>
                </Suspense>
            </QueryClientProvider>
        </ChakraProvider>
    );
};

App.displayName = "App";
export default App;
