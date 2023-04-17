import { render, screen } from '@testing-library/react';
import '@testing-library/jest-dom'
import React from 'react';
import App from '../App';
import About from '../components/about/About';
import Badges from '../components/badges/Badges';

test('Main page renders correctly', () => {
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
  expect(screen.getByTestId('Learn More Paweł')).toBeDefined()
  expect(screen.getByTestId('Learn More Michał')).toBeDefined()
  expect(screen.getByTestId('Learn More Kasia')).toBeDefined()
  
})

test('Badges page renders correctly', () => {
  render(<Badges />)
  expect(screen.getByText('Sprawności Łącznościowe')).toBeInTheDocument()
  expect(screen.getByText('Sprawności Kucharskie')).toBeInTheDocument()
  expect(screen.getByText('Sprawności Przyrodnicze')).toBeInTheDocument()
  expect(screen.getByText('Sprawności Wyrobienie Harcerskie')).toBeInTheDocument()
  
})
