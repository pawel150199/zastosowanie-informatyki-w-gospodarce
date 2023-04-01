import { render, screen } from '@testing-library/react';
import '@testing-library/jest-dom'
import App from '../App';
import About from '../components/about/About';

test('Main app show corectly', () => {
  render(<App />)
  const textElemnt = screen.getByText('Witaj w aplikacji Harcownik')
  expect(textElemnt).toBeInTheDocument()
  
})

test('Raport is avaible', () => {
  render(<App />)
  const textElemnt = screen.getByText('Czym jest Harcownik?')
  expect(textElemnt).toBeInTheDocument()
  
})

test('About page renders correctly', () => {
  render(<About />)
  const textElement = screen.getByText('Harcownik to aplikacja webowa skierowana do organizacji harcerskich. Ma ona za zadanie usprawnić zarządzanie harcerzykami.')
  expect(textElement).toBeInTheDocument()
})