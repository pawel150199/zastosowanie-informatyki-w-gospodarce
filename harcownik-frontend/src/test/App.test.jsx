import { render, screen } from '@testing-library/react';
import '@testing-library/jest-dom'
import App from '../App';
import About from '../components/about/About';
import UserPage from '../components/user/User';

test('Main app show corectly', () => {
  render(<App />)
  expect(screen.getByText('Witaj w aplikacji Harcownik')).toBeInTheDocument()
  expect(screen.getByText('Czym jest Harcownik?')).toBeInTheDocument()
  expect(screen.getByText('Features')).toBeInTheDocument()
  
})

test('About page renders correctly', () => {
  render(<About />)
  expect(screen.getByText('Harcownik to aplikacja webowa skierowana do organizacji harcerskich. Ma ona za zadanie usprawnić zarządzanie harcerzykami.')).toBeInTheDocument()
  expect(screen.getByText('Harcownik')).toBeInTheDocument()
  expect(screen.getByText('Nasz zespół')).toBeInTheDocument()
})